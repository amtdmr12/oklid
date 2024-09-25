import math

# Noktalar listesi
points = [(1, 2), (4, 6), (7, 8), (2, 5)]

# Öklid mesafesi hesaplama fonksiyonu
def euclideanDistance(point1, point2):
    x1, y1 = point1
    x2, y2 = point2
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

# Mesafeleri hesaplama
distances = []

for i in range(len(points)):
    for j in range(i + 1, len(points)):
        distance = euclideanDistance(points[i], points[j])
        distances.append(distance)

# Minimum mesafeyi bulma
min_distance = min(distances)
print(f"Minimum Mesafe: {min_distance}")