library(shiny)
library(shinyBS)
library(shape)


ui <- shinyUI(fluidPage(
  tags$title("Proiect PS: Chaos Game"),
  tags$h3("Proiect PS: Chaos Game"),
  sidebarLayout(
    sidebarPanel (
      selectizeInput(
        'shape',
        h5(tags$b('Shape')),
        choices = list("Forme" = c(
          `Triunghi` = 'tri', `Pentagon` = 'pent'
        )),
        selected = 'tri'
      ),
      conditionalPanel(
        condition = "input.shape=='tri'",
        sliderInput(
          inputId = "dist.tri",
          label = h5(tags$b("Ratie Distanta:")),
          min = 0.01,
          max = .99,
          value = .50,
          step = .01
        ),
        div("Ratia default este: 0.50",
            style = "font-size: 9.5pt;color:teal", align = "left")
      ),
      
      conditionalPanel(
        condition = "input.shape=='pent'",
        sliderInput(
          inputId = "dist.pent",
          label = h5(tags$b("Ratie Distanta:")),
          min = 0.01,
          max = .99,
          value = .63,
          step = .01
        ),
        div("Ratia default 0.63", style = "font-size: 9.5pt;color:teal", align =
              "left")
      ),
      br(),
      div(uiOutput("my.pts")),
      br(),
      div(bsButton("generate", label = "Randomize"), align = "right")
    ),
    mainPanel("Vizualizare", value = 3,
              fluidRow(
                  div(div(
                    plotOutput("compPlot")
                  ),
                  align = "center"),
                  HTML(
                    "<hr style='height: 2px; color: #BDBDBD; background-color: #D9D9D9; border: none;'>"
                  )
              ))
  )
))

# ------------------------------------------------------------------------------------------------------------

# Triunghi
tri.generate <- function(wt) {
  weight <- wt
  len <- 50000
  
  # matrice loc_index care contine toate endpointurile
  loc_index <- matrix(NA, ncol = 3, nrow = 3)
  
  loc_index[1, ] <- c(1, 0, 0)
  loc_index[2, ] <- c(2, 0.5, sqrt(3) / 2)
  loc_index[3, ] <- c(3, 1, 0)
  
  # lista cu toate punctele de intalnire
  vertices <- runif(len)
  vertices[which(vertices > 2 / 3)] <- 3
  vertices[which(1 / 3 < vertices & vertices <= 2 / 3)] <- 2
  vertices[which(vertices <= 1 / 3)] <- 1
  
  coords <- matrix(NA, ncol = 2, nrow = (len + 1))
  colnames(coords) <- c("x", "y") # ggvis
  
  coords[1, ] <- c(runif(1), runif(1) * sqrt(3) / 2)
  
  for (i in 1:len) {
    row <- i + 1
    spot <- vertices[i]
    x <- loc_index[spot, 2]
    y <- loc_index[spot, 3]
    x.new <- weight * x + (1 - weight) * coords[i, 1]
    y.new <- weight * y + (1 - weight) * coords[i, 2]
    coords[row, ] <- c(x.new, y.new)
    x <- x.new
    y <- y.new
  }
  return(list(loc_index, vertices, coords))
}

# Pentagon
pent.generate <- function(wt) {
  weight <- wt
  len <- 50000
  loc_index <- matrix(NA, ncol = 3, nrow = 5)
  
  c1 <- 0.25 * (sqrt(5) - 1)
  c2 <- 0.25 * (sqrt(5) + 1)
  s1 <- 0.25 * (sqrt(10 + 2 * sqrt(5)))
  s2 <- 0.25 * (sqrt(10 - 2 * sqrt(5)))
  
  loc_index[1, ] <- c(1, 0, 1)
  loc_index[2, ] <- c(2, s1, c1)
  loc_index[3, ] <- c(3, s2, -c2)
  loc_index[4, ] <- c(4, -s2, -c2)
  loc_index[5, ] <- c(5, -s1, c1)
  
  vertices <- runif(len)
  vertices[which(vertices > 4 / 5)] <- 5
  vertices[which(3 / 5 < vertices & vertices <= 4 / 5)] <- 4
  vertices[which(2 / 5 < vertices & vertices <= 3 / 5)] <- 3
  vertices[which(1 / 5 < vertices & vertices <= 2 / 5)] <- 2
  vertices[which(vertices <= 1 / 5)] <- 1
  
  coords <- matrix(NA, ncol = 2, nrow = (len + 1))
  colnames(coords) <- c("x", "y") # ggvis
  
  # coordonatele alese random
  coords[1, ] <- c(runif(1, -s1, s1), runif(1, -c2, 1))
  
  for (i in 1:len) {
    row <- i + 1
    spot <- which(loc_index[, 1] == vertices[i])
    x <- loc_index[spot, 2]
    y <- loc_index[spot, 3]
    x.new <- (weight) * x + (1 - weight) * coords[i, 1]
    y.new <- (weight) * y + (1 - weight) * coords[i, 2]
    coords[row, ] <- c(x.new, y.new)
  }
  return(list(loc_index, vertices, coords))
}



# ------------------------------------------------------------------------------------------------------------

server <- shinyServer(function(input, output, session) {
  output$my.pts <- renderUI({
    input$shape
    sliderInput(
      "pts",
      "Numar de puncte:",
      min = 1000,
      max = 50000,
      step = 1000,
      value = 5000,
      animate = animationOptions(interval = 200)
    )
  })
  
  updateButton(
    session,
    "generate",
    style = "primary",
    size = "default",
    disabled = FALSE
  )
  
  all.list <- reactive({
    if (input$shape == "tri") {
      return(tri.generate(input$dist.tri * (input$generate > -1)))
    }
    if (input$shape == "pent") {
      return(pent.generate(input$dist.pent * (input$generate > -1)))
    }
  })
  
  output$compPlot <- renderPlot({
    loc_index <- all.list()[[1]]
    # vertices  <- all.list()[[2]]
    coords    <- all.list()[[3]]
    
    # Triunghi
    if (input$shape == "tri") {
      # par(mar = c(0.5, 0.5, 0.5, 0.5))
      plot(
        0,
        0,
        xlim = c(0, 1),
        ylim = c(0, sqrt(3) / 2),
        col = 0,
        yaxt = "n",
        xaxt = "n",
        xlab = "",
        ylab = "",
        bty = "n"
      )
    }
    
    # Pentagon
    if (input$shape == "pent") {
      c1 <- 0.25 * (sqrt(5) - 1)
      c2 <- 0.25 * (sqrt(5) + 1)
      s1 <- 0.25 * (sqrt(10 + 2 * sqrt(5)))
      s2 <- 0.25 * (sqrt(10 - 2 * sqrt(5)))
      
      # par(mar = c(0.5, 0.5, 0.5, 0.5))
      plot(
        0,
        0,
        xlim = c(-s1, s1),
        ylim = c(-c2, 1),
        col = 0,
        yaxt = "n",
        xaxt = "n",
        xlab = "",
        ylab = "",
        bty = "n"
      )
    }
    
    if (!is.null(input$pts)) {
      if (input$pts != 0) {
        points(coords[1:input$pts, 1],
               coords[1:input$pts, 2],
               pch = ".",
               cex = 2.5,
               col = "blue")
      }
    }
    points(
      loc_index[, 2],
      loc_index[, 3],
      pch = 20,
      cex = 2,
      col = "red"
    )
  })
})

shinyApp(ui = ui, server = server)
