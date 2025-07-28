library(gapminder)

r_log <- function(message) {
    cat("example output from gapminder:\n")
    print(head(gapminder))
    faasr_log(message)
}
