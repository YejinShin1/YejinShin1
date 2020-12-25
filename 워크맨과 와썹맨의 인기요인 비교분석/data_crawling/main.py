#!/usr/bin/env python
# coding: utf-8

# In[2]:


import sys
import youtube_crawler


# In[ ]:


youtube_crawler.video_url_crawling()          # 유튜브에 있는 동영상 제목, url 전부 가져옴
youtube_crawler.video_comment_crawling()     # 유튜브 각 동영상에 있는 댓글 전부 가져옴

