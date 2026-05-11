library(knitr)
library(tidyverse)
library(ggplot2)
library(readxl)
library(ggpubr)

MutationRates = read_csv("MutationRate.csv")

MutationRates %>%
  ggplot(aes(x = Genotype, y = MutationRate)) +
  geom_boxplot() +
  #stat_summary(fun = mean, geom = "bar") +
  stat_summary(fun.data = mean_se, geom = "errorbar", width = 0.2) +
  facet_grid(Genome ~ MutationType) +
  labs(y = "Mutation Rate") +
  scale_y_log10() +
  theme_bw()

