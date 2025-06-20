#%%
import os
import requests
from dotenv import load_dotenv

#%%
load_dotenv()
ACCESS_TOKEN = os.getenv("ZENODO_ACCESS_TOKEN")
record_id = "14223624" #LUNA25 record id

# Specify the output folder where files will be saved
output_folder = "D:\project_data"
os.makedirs(output_folder, exist_ok=True)

# Get the metadata of the Zenodo record
r = requests.get(f"https://zenodo.org/api/records/{record_id}", params={'access_token': ACCESS_TOKEN})

if r.status_code != 200:
    print("Error retrieving record:", r.status_code, r.text)
    exit()

# Extract download URLs and filenames
download_urls = [f['links']['self'] for f in r.json()['files']]
filenames = [f['key'] for f in r.json()['files']]

print(f"Total files to download: {len(download_urls)}")

#%% Download each file
for index, (filename, url) in enumerate(zip(filenames, download_urls)):
    file_path = os.path.join(output_folder, filename)

	# check if file already exists
    if os.path.exists(file_path):
          print(f"File {filename} already exists, skipping download.")
          continue

    # only download the files that end in 001, 0105, 013, 020
    # if not filename.endswith(('007', '024')):
        #print(f"File {filename} does not match the criteria, skipping download.")
    #    continue

    print(f"Downloading file {index}/{len(download_urls)}: {filename} -> {file_path}")

    with requests.get(url, params={'access_token': ACCESS_TOKEN}, stream=True) as r:
        r.raise_for_status()  # Raise an error for failed requests
        with open(file_path, 'wb') as f:
            for chunk in r.iter_content(chunk_size=8192):  # Download in chunks
                f.write(chunk)

    print(f"Completed: {filename}")

print("All downloads completed successfully!")
 # %%
