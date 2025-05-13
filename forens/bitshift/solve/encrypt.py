def increment_png_bytes(input_path, output_path):
    try:
        # Read the original PNG file as binary
        with open(input_path, 'rb') as f:
            png_data = bytearray(f.read())
        
        # Increment each byte by 1 (mod 256 to handle overflow)
        modified_data = bytearray((b - 1) % 256 for b in png_data)
        
        # Write the modified data to a new file
        with open(output_path, 'wb') as f:
            f.write(modified_data)
            
        print(f"Successfully created modified PNG at {output_path}")
        return True
    
    except Exception as e:
        print(f"Error: {e}")
        return False

# Example usage:
input_png = "picopico.png"
output_png = "orig.png"
increment_png_bytes(input_png, output_png)