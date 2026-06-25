import subprocess
import sys
import shutil
import os


# -------------------------
# Run Tests
# -------------------------
print("Running Tests...")

test_result = subprocess.run(["pytest"])

if test_result.returncode != 0:
    print("Tests Failed")
    sys.exit(1)

print("Tests Passed")


# -------------------------
# Run Lint
# -------------------------
print("\nRunning Lint...")

lint_result = subprocess.run(["ruff", "check", "."])

if lint_result.returncode != 0:
    print("Lint Failed")
    sys.exit(1)

print("Lint Passed")

print("\nPipeline Successful")

print("\nBuilding Artifact...")

# Clean old build folder
if os.path.exists("build"):
    shutil.rmtree("build")

# Create fresh build folder
os.makedirs("build")

# Copy runtime files
shutil.copy("calculator.py", "build/")
shutil.copy("requirements.txt", "build/")

print("Build folder prepared")

# Create dist folder
os.makedirs("dist", exist_ok=True)

# Remove old artifact if present
artifact_path = "dist/artifact.zip"

if os.path.exists(artifact_path):
    os.remove(artifact_path)

# Create ZIP from build folder
shutil.make_archive(
    "dist/artifact",
    "zip",
    "build"
)

print("Artifact Created")