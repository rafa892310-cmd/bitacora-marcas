import os
import zipfile

# Crear estructura de carpetas
base_dir = "imagenes-marcas"
brands = ["samsung", "redmi", "poco", "motorola", "infinix", "zte", "oppo"]

os.makedirs(base_dir, exist_ok=True)
for brand in brands:
    folder = os.path.join(base_dir, brand)
    os.makedirs(folder, exist_ok=True)
    with open(os.path.join(folder, ".gitkeep"), "w") as f:
        f.write("")

# Crear README.md
readme_content = """# 📸 Repositorio de Imágenes por Marca

Este repositorio contiene imágenes organizadas por marca de celular.

## Carpetas
- 📁 samsung/
- 📁 redmi/
- 📁 poco/
- 📁 motorola/
- 📁 infinix/
- 📁 zte/
- 📁 oppo/
"""
with open(os.path.join(base_dir, "README.md"), "w", encoding="utf-8") as f:
    f.write(readme_content)

# Crear el archivo ZIP
zip_filename = "imagenes-marcas.zip"
with zipfile.ZipFile(zip_filename, "w", zipfile.ZIP_DEFLATED) as zipf:
    for root, _, files in os.walk(base_dir):
        for file in files:
            filepath = os.path.join(root, file)
            arcname = os.path.relpath(filepath, os.path.dirname(base_dir))
            zipf.write(filepath, arcname=arcname)

print(f"Archivo ZIP creado: {zip_filename}")