from module.readCSV import readCSV
from module.songList import songList
from module.filterCommas import filterCommas
from module.fetchVideoUrl import fetchVideoUrl
from module.urlFormatter import urlFormatter
from module.downloadSongs import downloadSongs

from controls import controls

def main():
  location = input("Where is the CSV located: ")
  output = input("Where should the music be output: ")
  
  controller = controls(location, output)
  
  # Returns a pandas dataframe
  csv = readCSV(controller.fileLocation)
  if not csv["status"]:
    return csv["response"]
  
  # csv is a dict, response is the dataframe
  csvFile = csv["response"]

  # List of dicts that stores songs and artists
  songDicts = songList(csvFile)
  
  # Ditto but with artists and commas split
  filteredSongDicts = filterCommas(songDicts)
  
  # Turns those song names and artists into url codes
  urlList = fetchVideoUrl(filteredSongDicts, controller)
  
  # This turns the URL codes into youtube URLs
  formattedUrlList = urlFormatter(urlList)

  print(formattedUrlList)
  fileLocations = []
  for i in formattedUrlList:
    if i["confident"] == False:
      if not input(f"Input nothing to confirm URL {i["url"]}"):
        response = downloadSongs(i, controller)
        fileLocations.append(response)
    else:
      response = downloadSongs(i, controller)
      fileLocations.append(response)
  print(fileLocations)

  return "Successfully ran the application"

if __name__ == "__main__":
  status = main()
  print(status)