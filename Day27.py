import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import re

st.set_page_config(page_title="Social Media Trend Analyzer", page_icon="📊")
st.title("📊 Social Media Trend Analyzer")

file = st.file_uploader("Upload CSV", type="csv")
if not file:
    st.info("Upload a CSV file to start.")
    st.stop()

df = pd.read_csv(file)

st.sidebar.header("🔎 Filters")
cats = st.sidebar.multiselect("Category", df.Category.unique(), default=list(df.Category.unique()))
users = st.sidebar.multiselect("User", df.User.unique(), default=list(df.User.unique()))
df = df[df.Category.isin(cats) & df.User.isin(users)].copy()

df["Engagement"] = df.Likes + df.Comments + df.Shares

a,b,c,d = st.columns(4)
a.metric("Posts", len(df))
b.metric("Likes", int(df.Likes.sum()))
c.metric("Engagement", int(df.Engagement.sum()))
d.metric("Avg Engagement", round(df.Engagement.mean(),2))

st.subheader("🔥 Top Trending Hashtags")
hashtags = df.Hashtags.str.findall(r"#\w+").explode().value_counts().head(10)
fig,ax=plt.subplots()
hashtags.sort_values().plot(kind="barh",ax=ax)
ax.set_xlabel("Posts")
st.pyplot(fig)

st.subheader("👥 Most Active Users")
st.dataframe(df.User.value_counts().rename("Posts").reset_index(),use_container_width=True)

st.subheader("📈 Daily Engagement Trend")
daily=df.groupby("Date").Engagement.sum()
fig,ax=plt.subplots()
daily.plot(kind="line",marker="o",ax=ax)
ax.set_ylabel("Engagement")
ax.grid(True,alpha=.3)
st.pyplot(fig)

st.subheader("🍱 Content Category Distribution")
fig,ax=plt.subplots()
df.Category.value_counts().plot(kind="bar",ax=ax)
ax.set_ylabel("Posts")
plt.xticks(rotation=30)
st.pyplot(fig)

st.subheader("⏰ Most Popular Posting Time")
df["Hour"]=pd.to_datetime(df.Time,format="%H:%M").dt.hour
hours=df.groupby("Hour").Engagement.sum()
h=hours.idxmax()
st.success(f"Most popular posting hour: {h:02d}:00")

st.subheader("😊 Sentiment Analysis")
positive=["amazing","great","fantastic","love","loved","excellent","useful","good","happy"]
negative=["bad","poor","disappointing","disappointed","frustrating","hate","hated","worst"]

def sentiment(x):
    words=re.findall(r"\b\w+\b",str(x).lower())
    p=sum(w in positive for w in words)
    n=sum(w in negative for w in words)
    return "Positive" if p>n else "Negative" if n>p else "Neutral"

df["Sentiment"]=df.Text.apply(sentiment)
fig,ax=plt.subplots()
df.Sentiment.value_counts().plot(kind="bar",ax=ax)
st.pyplot(fig)

st.subheader("📥 Export Analytics Report")
st.download_button("Download CSV",df.to_csv(index=False),"social_media_analytics_report.csv","text/csv")