# Justin Kilchenmann calculating variance and standard deviation

points = [109, 120, 136, 135, 116, 112, 123, 135, 124, 104, 128, 137, 123, 132, 131, 131, 123, 131, 132, 133, 127, 133, 109, 129, 111, 129, 133, 94, 135, 113, 120, 131, 127, 128, 102, 136, 134, 115, 137, 127, 125, 130, 132, 132, 127, 30, 129, 138, 110, 134, 135, 131, 111, 137, 131, 134, 118, 109, 129, 127, 131, 128, 123, 113, 137, 135, 138, 138, 134, 131, 134, 132, 133, 134, 108, 127, 134, 107, 98, 130, 135, 77, 125, 87, 106, 136, 135, 135, 136, 97, 106, 104, 137, 128, 134, 130, 131, 60, 118, 123, 137, 136, 120, 110, 131, 135, 126, 122, 121, 101, 137, 138, 92, 119, 134, 129, 130, 105, 121, 131, 134, 66, 122, 113, 116, 130, 130, 130, 138, 131, 135, 136, 136, 132, 135, 124, 125, 124, 123, 126, 136, 138, 128, 101, 123, 61, 133, 134, 121, 130, 120, 137]

import statistics

# Display results
print ('Variance: ', statistics.pvariance(points))
print ('Standard Deviation: ', statistics.pstdev(points))