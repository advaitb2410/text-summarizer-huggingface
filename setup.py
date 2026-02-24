import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()
AUTHOR_USER_NAME = "advaitbhattp"
REPO_NAME = "text-summarizer-huggingface"

setuptools.setup(
    name="text-summarizer-huggingface",
    version="0.1.0",
    author="advaitbhattp@gmail.com",
    author_email="<EMAIL_ADDRESS>",
    description="A text summarization tool using Hugging Face transformers.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
)