import streamlit as st
import pandas as pd


st.title("Projects for you")
df = pd.DataFrame(
    [
        {"Name": "port of mars", "Links": "https://github.com/topics/space-exploration"},
        {"Name": "spacewalk", "Links": "https://github.com/spacewalkproject/spacewalk"},
        {"Name": "PlanetProspect", "Links": "https://github.com/YassenEfremov/PlanetProspect"},
        {"Name": "astrodata", "Links": "https://github.com/gvard/astrodata"},
        {"Name": "Solar System", "Links": "https://github.com/JT5519/Solar-System"},
        {"Name": "space debris", "Links": "https://github.com/galactic-embassy/space-debris"},
        {"Name": "  space launches", "Links": "https://github.com/Quartz/space-launches"},
    ]
)


st.dataframe(df, use_container_width=True)
