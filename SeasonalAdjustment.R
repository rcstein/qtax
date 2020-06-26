install.packages("seasonal")
install.packages("x13binary")
library(seasonal)
library(tidyverse)
setwd("~/Documents/Employ America/qtax/Data")
all_qtax <- read.csv("Qtax-edit.csv")
categories <- unique(all_qtax$Category)
states <- unique(all_qtax$State)

levels(states)[1]
vars = c('Period', 'Value')
california_totals <-  dplyr::filter(all_qtax, State == 'CA', Category == 'Total')[vars]
california_totals <-  ts(california_totals, start = c(1994,1), frequency = 4)


levels(states)[5]

ca <- seas(california_totals)
x13binary::checkX13binary()
?seasonal
Sys.setenv(X13_PATH = "~/Documents/Employ America/qtax/Data")
