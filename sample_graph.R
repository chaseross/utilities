setwd(path.expand("~/path/to/output/folder") )
sample_data <- read.csv("~/path/to/input/file")
head(sample_data)
pdf("sample_plot.pdf", width = 4, height = 4)
hist(sample_data$value)
dev.off()
