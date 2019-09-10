
# Calculate Pi
pi_function <- function(d, x) {
  if (d > x) {
    return(d-x);
  } else {
    return(0);
  }
  
}

# V(t)
v_function <- function(X_set, t, m, T_max) {
  d = 5
  K = 20
  h = 1
  vector <- integer(length(X_set))
  for (x in X_set) {
    
    vi = x+1
    
    if (t == T_max) {
      vector[vi] <- 0;
      next
    }
    pi <- pi_function(d, x);
    
    indic = 0
    if (pi > 0) {
      indic = 1
    }

    Vtnext = x - d + pi
    tnext = t+1
    VtnextVal = m[Vtnext + 1, tnext + 1]
    vector[vi] = K*indic + h*x + VtnextVal
    
  }
  m[,t+1] = vector

  return(m)
}

X_set = c(seq(0, 50))
T_max=1000
time_range = T_max + 1
x_range = max(X_set)
m <- matrix(, ncol=time_range, nrow=x_range+1, , dimnames = list(X_set,  c(seq(0, T_max))))
for (t in T_max:0) {
  # Calculate V with different Ordersizes (X) for each T
  m = v_function(X_set, t, m, T_max)  
}

m[,1]
min(m[,1])

