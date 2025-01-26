import sys
import os
import subprocess

# Check if correct arguments are passed
if len(sys.argv) != 4:
    print("Usage: python apk_injector.py <APK_PATH> <PAYLOAD> <OUTPUT_APK>")
    sys.exit(1)

apk_path = sys.argv[1]
payload_file = sys.argv[2]
output_apk = sys.argv[3]

# Step 1: Decompile APK
print("Decompiling APK...")
subprocess.run(['apktool', 'd', apk_path])

# Step 2: Inject Payload
print("Injecting payload...")
# Add your payload injection logic here (this can vary based on the tool)

# Step 3: Recompile the APK
print("Recompiling APK...")
subprocess.run(['apktool', 'b', os.path.splitext(apk_path)[0], '-o', output_apk])

# Step 4: Sign APK
print("Signing APK...")
subprocess.run(['jarsigner', '-verbose', '-sigalg', 'SHA1withRSA', '-digestalg', 'SHA-1',
                '-keystore', 'my-release-key.keystore', os.path.join(os.path.splitext(apk_path)[0], 'dist', 'classes.dex'), 'alias_name'])

print(f"Malicious APK saved to {output_apk}")
