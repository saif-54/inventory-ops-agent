from PIL import Image, ImageDraw

# Create canvas (1080x1350 - Instagram/E-commerce portrait)
img = Image.new('RGB', (1080, 1350), color=(245, 245, 242))
draw = ImageDraw.Draw(img)

# Draw card frame and bottom info banner
draw.rectangle([100, 100, 980, 1100], fill=(225, 220, 215), outline=(180, 170, 160), width=4)
draw.rectangle([100, 1150, 980, 1300], fill=(30, 30, 30))

draw.text((150, 1180), "Abaya Brand - Prototype Card", fill=(255, 255, 255))
draw.text((150, 1220), "Resolution: 1080x1350 | Optimized Web Engine", fill=(200, 200, 200))

output_path = "C:/Users/saifh/agent_workspace/sample_abaya_card.jpg"
img.save(output_path, quality=90)
print(f"\n--- Image Processed Successfully ---\nSaved: {output_path}\nDimensions: 1080x1350\n")