# step4_recommend_colors.py

def recommend_outfit_colors(skin_rgb):
    r, g, b = skin_rgb

    # Convert to HSV for better analysis
    import colorsys
    h, s, v = colorsys.rgb_to_hsv(r/255, g/255, b/255)
    h_deg = h * 360

    print(f"Skin Hue: {round(h_deg)}°, Saturation: {round(s*100)}%, Brightness: {round(v*100)}%")

    recommendations = []

    # Simple rule-based mapping using color theory
    if v < 0.4:
        # Dark skin tones
        recommendations = ['White', 'Cream', 'Sky Blue', 'Yellow', 'Lavender']
    elif v > 0.75:
        # Fair/light skin tones
        recommendations = ['Navy Blue', 'Emerald Green', 'Burgundy', 'Charcoal Grey']
    else:
        # Medium/neutral skin tones
        recommendations = ['Coral', 'Teal', 'Olive Green', 'Rust Orange', 'Purple']

    print("\nRecommended Outfit Colors:")
    for color in recommendations:
        print("-", color)

    return recommendations

if __name__ == "__main__":
    from step3_cluster_skin_color import extract_skin_color

    skin_rgb = extract_skin_color("face_capture.jpg")
    recommend_outfit_colors(skin_rgb)
