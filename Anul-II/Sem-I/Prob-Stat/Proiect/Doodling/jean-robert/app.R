library(shiny)
library(gmp)

drawStar <-
  function(center,
           length,
           pts,
           direction = 0,
           segments = F,
           colour = F) {
    if (length(pts) == 0)
      return()
    if (segments & (pts[1] == 2))
      direction <- direction + pi / 2
    for (i in 1:pts[1]) {
      point <- center +
        length * c(cos(direction + pi / 2 + i * 2 * pi / pts[1]),
                   sin(direction + pi / 2 + i * 2 * pi / pts[1]))
      if (!segments) {
        if (length(pts) == 1)
          if (colour) {
            points(
              x = point[1],
              y = point[2],
              pch = 20,
              col = rainbow(pts[1])[i]
            )
          } else {
            points(x = point[1],
                   y = point[2],
                   pch = 20)
          }
        nextdirection <- 0
        if (pts[1] == 2)
          nextdirection <- direction + pi / 2
        if (length(pts) > 1)
          if ((pts[1] != 2) &
              (pts[2] == 2))
            nextdirection <- direction + i * 2 * pi / pts[1]
      } else {
        if (colour) {
          lines(
            x = c(center[1], point[1]),
            y = c(center[2], point[2]),
            col = rainbow(10)[pts[1] %% 10],
            lwd = 2
          )
        } else {
          lines(x = c(center[1], point[1]),
                y = c(center[2], point[2]))
        }
        nextdirection <- direction + i * 2 * pi / pts[1]
      }
      drawStar(
        center = point,
        length = length / ((pts[1]) ^ (1 / 1.25)),
        pts = pts[-1],
        direction = nextdirection,
        segments = segments,
        colour = colour
      )
    }
  }

makePFV <-
  function(N,
           segments = F,
           colour = F,
           direction = 0,
           order = 'desc') {
    plot(
      x = c(-1.5, 1.5),
      y = c(1.5, -1.5),
      pch = '',
      xlab = '',
      ylab = '',
      asp = 1,
      bty = 'n',
      axes = F
    )
    primes <- switch(
      order,
      asc = as.numeric(factorize(N)),
      desc = rev(as.numeric(factorize(N))),
      rand = sample(as.numeric(factorize(N)))
    )
    drawStar(
      center = c(0, 0),
      length = 1,
      direction = direction,
      pts = primes,
      segments = segments,
      colour = colour
    )
  }

shinyServer(function(input, output) {
  output$caption <- reactiveText(function() {
    paste(input$N, '=', paste(as.numeric(factorize(input$N)), collapse = 'x'))
  })
  
  output$visuPlot <- reactivePlot(function() {
    makePFV(
      N = input$N,
      segments = ifelse(input$segments == 'yes', T, F),
      colour = ifelse(input$colour == 'yes', T, F),
      direction = input$direction * 2 * pi / 360
    )
  })
})

ui.R:library(shiny)

# Define UI for application that plots random distributions
shinyUI(pageWithSidebar(
  # Application title
  headerPanel("Prime Factorization Visualization"),
  
  # Sidebar with a slider input for number of observations
  sidebarPanel(
    numericInput("N", "Number to visualize:", 2 * 3 * 3 * 7),
    
    radioButtons("colour", "Colours?",
                 list("Yes" = 'yes',
                      "No" = 'no')),
    
    radioButtons("segments", "Segments?",
                 list("Yes" = 'yes',
                      "No" = 'no')),
    
    sliderInput(
      "direction",
      "Orientation:",
      min = -360,
      max = 360,
      value = 0
    )
  ),
  
  # Show a plot of the generated distribution
  mainPanel(h3(textOutput("caption")),
            
            plotOutput("visuPlot"))
))

