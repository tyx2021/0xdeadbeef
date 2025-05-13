def decrement_png_bytes(input_path, output_path):
    try:
        # Read the modified PNG file as binary
        with open(input_path, 'rb') as f:
            modified_data = bytearray(f.read())
        
        # Decrement each byte by 1 (mod 256 to handle underflow)
        original_data = bytearray((b - 1) % 256 for b in modified_data)
        
        # Write the restored data to a new file
        with open(output_path, 'wb') as f:
            f.write(original_data)
            
        print(f"Successfully restored original PNG at {output_path}")
        return True
    
    except Exception as e:
        print(f"Error: {e}")
        return False

# Example usage:
corrupted_png = "modified.png"
restored_png = "restored.png"
decrement_png_bytes(corrupted_png, restored_png)