library(RCurl)
library(RJSONIO)
library(plyr)
setwd('/var/www/freq_api')

url <- function(address, return.call = "json", sensor = "false") {
  root <- "http://maps.google.com/maps/api/geocode/"
  u <- paste(root, return.call, "?address=", address, "&sensor=", sensor, sep = "")
  return(URLencode(u))
}

geoCode <- function(address,verbose=FALSE) {
  if(verbose) cat(address,"\n")
  u <- url(address)
  doc <- getURL(u)
  x <- fromJSON(doc,simplify = FALSE)
  if(x$status=="OK") {
    lat <- x$results[[1]]$geometry$location$lat
    lng <- x$results[[1]]$geometry$location$lng
    return(c(lat, lng))
  } else {
    return(c(NA,NA))
  }
}

data<-read.table("test.txt")
x<-apply(data, 1, geoCode)
data<-cbind(data, t(x))
write.table(data, file="out.txt", sep="\t", row.names=FALSE, col.names=FALSE, quote=FALSE)
