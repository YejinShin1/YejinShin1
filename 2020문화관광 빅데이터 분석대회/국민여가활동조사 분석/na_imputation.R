setwd("C:/Users/Rstudio/Desktop/문화분석/국민여가활동조사")
library(dplyr)
library(dlookr)
library(tidyverse)
data2019 <- read.csv("C:/Users/Rstudio/Desktop/문화분석/국민여가활동조사/data2019_rev.csv")

x<-imputate_na(data2019,Attr20,Satisf,method="rpart")
write.csv(rpart_data, "C:/Users/Rstudio/Desktop/문화분석/국민여가활동조사/data2019_rpart_log.csv")

