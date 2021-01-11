library(datasets)
library(GGally)
library(ggplot2)

data(iris)
View(iris)

unique(iris$Species)


ggpairs(iris, mapping=ggplot2::aes(colour = Species))


x = rnorm(100)
y = rnorm(100,sd=2)

df = data.frame(x,y)

myplot <- ggplot(df,aes(x=x,y=y))

myplot + geom_point() + xlab('X points') + ylab("Y points")

