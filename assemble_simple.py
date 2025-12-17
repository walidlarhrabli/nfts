from PIL import Image
import os

# Créer dossier output
os.makedirs('output', exist_ok=True)

# Chemins des dossiers
backgrounds_folder = r'C:\Users\HP\Downloads\pepustars_collection\layers/1_backgrounds/common'
characters_folder = r'C:\Users\HP\Downloads\pepustars_collection\layers/2_bodies/standard'

print("🚀 Génération Multiple...\n")

# Lister tous les backgrounds
backgrounds = [f for f in os.listdir(backgrounds_folder) if f.endswith('.png')]
print(f"✓ {len(backgrounds)} backgrounds trouvés:")
for bg in backgrounds:
    print(f"  - {bg}")

print()

# Lister tous les characters
characters = [f for f in os.listdir(characters_folder) if f.endswith('.png')]
print(f"✓ {len(characters)} characters trouvés:")
for char in characters:
    print(f"  - {char}")

print(f"\n📊 TOTAL À GÉNÉRER: {len(characters)} × {len(backgrounds)} = {len(characters) * len(backgrounds)} images\n")
print("="*60)

# Compteur
count = 1

# Pour chaque character
for char_file in characters:
    char_name = char_file.replace('.png', '')
    char_path = os.path.join(characters_folder, char_file)
    
    # Charger le character une fois
    character = Image.open(char_path).convert('RGBA')
    
    # Redimensionner si nécessaire
    if character.size != (1000, 1000):
        character = character.resize((1000, 1000))
    
    # Pour chaque backgrouee
    for bg_file in backgrounds:
        bg_name = bg_file.replace('.png', '')
        bg_path = os.path.join(backgrounds_folder, bg_file)
        
        # Charger background
        background = Image.open(bg_path).convert('RGBA')
        
        # Redimensionner si nécessair
        if background.size != (1000, 1000):
            background = background.resize((1000, 1000))
        
        # Créer canvas et composer
        canvas = Image.new('RGBA', (1000, 1000))
        canvas = Image.alpha_composite(canvas, background)
        canvas = Image.alpha_composite(canvas, character)
        
        # Nom du fichier output
        output_name = f"{count:03d}_{char_name}_{bg_name}.png"
        output_path = os.path.join('output', output_name)
        
        # Sauvegarder
        canvas.save(output_path)
        
        print(f"✓ [{count}/{len(characters) * len(backgrounds)}] {output_name}")
        count += 1

print("="*60)
print(f"\n✅ TERMINÉ ! {count-1} images générées dans 'output/'")