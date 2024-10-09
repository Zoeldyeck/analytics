import streamlit as st
import streamlit.components.v1 as components

# Add Google Analytics tracking code using custom HTML
GA_TRACKING_ID = "G-P7D2VEJGE6"  # Replace with your Google Analytics Tracking ID

# Embedding Google Analytics script in Streamlit
google_analytics_code = f"""
<!-- Google tag (gtag.js) -->
<script async src="https://www.googletagmanager.com/gtag/js?id={GA_TRACKING_ID}"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){{dataLayer.push(arguments);}}
  gtag('js', new Date());
  gtag('config', '{GA_TRACKING_ID}');
</script>
"""

# Using Streamlit's components.html to inject the code
components.html(google_analytics_code)

# Your main Streamlit app
st.title("My Streamlit App with Google Analytics")
st.write("This app is being tracked using Google Analytics.")
