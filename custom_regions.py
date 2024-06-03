import json

# Fungsi untuk memisahkan provinsi berdasarkan region
def group_by_region(topojson_data):
    regions = {
        "Sumatera": ["Aceh", "Sumatera Utara", "Sumatera Barat", "Riau", "Kepulauan Riau", "Jambi", "Bengkulu", "Sumatera Selatan", "Lampung"],
        "Jawa Tengah - Jawa Barat": ["Jawa Tengah", "Jawa Barat", "Jakarta", "Yogyakarta", "Banten"],
        "Jawa Timur - Indonesia Timur": ["Jawa Timur", "Bali", "Nusa Tenggara Barat", "Nusa Tenggara Timur", "Maluku", "Maluku Utara", "Papua", "Papua Barat", "Kalimantan Barat", "Kalimantan Tengah", "Kalimantan Selatan", "Kalimantan Timur", "Kalimantan Utara", "Sulawesi Barat", "Sulawesi Selatan", "Sulawesi Tengah", "Sulawesi Tenggara", "Sulawesi Utara", "Gorontalo"],
    }
    
    grouped_data = {region: {"type": "Topology", "objects": {"provinces": {"type": "GeometryCollection", "geometries": []}}, "arcs": topojson_data["arcs"], "transform": topojson_data["transform"]} for region in regions}

    for geom in topojson_data["objects"]["provinces"]["geometries"]:
        provinsi = geom["properties"]["provinsi"]
        for region, provinces in regions.items():
            if provinsi in provinces:
                grouped_data[region]["objects"]["provinces"]["geometries"].append(geom)
                break
    return grouped_data

# Membaca data TopoJSON
with open('test.json', 'r') as f:
    topojson_data = json.load(f)

# Memisahkan data berdasarkan region
grouped_data = group_by_region(topojson_data)

# Menyimpan data TopoJSON untuk setiap region
for region, data in grouped_data.items():
    with open(f'topojson_{region.replace(" ", "_")}.json', 'w') as f:
        json.dump(data, f)
