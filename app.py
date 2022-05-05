import spacy_streamlit
import streamlit as st
import pandas as pd
import numpy as np

show_logo = False
models = ["ja_core_news_md", "ja_core_news_sm"]
default_text = "ここに日記を書いてね"
spacy_streamlit.visualize(models, default_text)