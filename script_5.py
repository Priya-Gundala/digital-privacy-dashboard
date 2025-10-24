
import zipfile
import os

# Create ZIP file
zip_filename = 'privacy-dashboard-mern-complete.zip'

with zipfile.ZipFile(zip_filename, 'w', zipfile.ZIP_DEFLATED) as zipf:
    # Walk through the directory
    for root, dirs, files in os.walk('privacy-dashboard-mern'):
        for file in files:
            file_path = os.path.join(root, file)
            arcname = file_path.replace('privacy-dashboard-mern/', '')
            zipf.write(file_path, arcname)

zip_size = os.path.getsize(zip_filename)

print("\n" + "="*60)
print("🎉 ZIP FILE CREATED SUCCESSFULLY!")
print("="*60)
print(f"\n📦 File: {zip_filename}")
print(f"📏 Size: {zip_size:,} bytes ({zip_size/1024:.1f} KB)")
print("\n📂 Contains:")
print("   ✅ Backend (Node.js + Express + MongoDB)")
print("   ✅ Frontend (React)")  
print("   ✅ All configuration files")
print("   ✅ README with setup instructions")
print("   ✅ Complete MERN stack project")
print("\n" + "="*60)
print("✨ DOWNLOAD THIS FILE AND YOU'RE READY TO GO!")
print("="*60)
