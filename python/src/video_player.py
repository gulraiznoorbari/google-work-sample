"""A video player class."""

from os import putenv
from .video_library import VideoLibrary
from .video_playlist import Playlist
import random

class VideoPlayer:
    """A class used to represent a Video Player."""

    def __init__(self):
        self.video_library = VideoLibrary()
        self.video_playlist = Playlist()
        self.current_video = None
        self.isPlaying = False
        self.isPaused = False

    def number_of_videos(self):
    
        num_videos = len(self.video_library.get_all_videos())
        print(f"{num_videos} videos in the library")

    
    def show_all_videos(self):
        """Returns all videos."""

        videos = self.video_library.get_all_videos()
        videos.sort(key=lambda x:x.title)
        flagged = self.video_library.flagged
        
        print("Here's a list of all available videos: ")
        for video in videos:
            tag = " ".join(video.tags)
            output = f" {video.title} ({video.video_id}) [{tag}]"
            if video.video_id in flagged:
                id = video.video_id
                output = output + f" - FLAGGED (reason: {flagged[id] if flagged[id] else 'Not supplied'})"
            print(output)


    def play_video(self, video_id):
        """Plays the respective video.
        
        Args:
            video_id: The video_id to be played.
        """
        
        video = self.video_library.get_video(video_id)
        flagged = self.video_library.flagged
        
        if video is None:
            print("Cannot play video: Video does not exist")       
        elif video_id in flagged:
                print(f"Cannot play video: Video is currently flagged (reason: {flagged[video_id] if flagged[video_id] else 'Not supplied'})")
        else:
            if self.isPlaying:
                print(f"Stopping video: {self.current_video.title}")
                self.isPaused = False
            
            print(f"Playing video: {video.title}")
            self.isPlaying = True
            self.current_video = video


    def stop_video(self):
        """Stops the current video."""

        if self.isPlaying is True:
            print(f"Stopping video: {self.current_video.title}")
            self.isPlaying = False
            self.isPaused = False
            self.current_video = None
        else:
            print("Cannot stop video: No video is currently playing")


    def play_random_video(self):
        """Plays a random video from the video library."""

        videos = list(filter(lambda x: (x.video_id not in self.video_library.flagged),self.video_library.get_all_videos()))
        number_of_videos = len(videos)
        
        if number_of_videos < 1:
            print("No videos available")
        else:
            if self.isPlaying is True:
                print(f"Stopping video: {self.current_video.title}")
                self.isPaused = False
        
            pick_video = random.choice(videos)
            print(f"Playing video: {pick_video.title}")
            self.isPlaying = True
            self.current_video = pick_video


    def pause_video(self):
        """Pauses the current video."""

        if self.isPaused:
            print(f"Video already paused: {self.current_video.title}")
        elif self.current_video is None:
            print("Cannot pause video: No video is currently playing")
        else:
            print(f"Pausing video: {self.current_video.title}")
            self.isPaused = True
            

    def continue_video(self):
        """Resumes playing the current video."""

        if self.current_video is not None:
            if not self.isPaused:
                print(f"Cannot continue video: Video is not paused")
            else:
                print(f"Continuing video: {self.current_video.title}")
        else:
            print("Cannot continue video: No video is currently playing")


    def show_playing(self):
        """Displays video currently playing."""

        if self.current_video == None:
            print("No video is currently playing")
        else:
            tag = " ".join(self.current_video.tags)
            output = f"Currently playing: {self.current_video.title} ({self.current_video.video_id}) [{tag}]"
            if self.isPaused == False:
                print(output)
            elif self.isPaused == True:
                print(f"{output} - PAUSED")
            else:
                print("No video is currently playing")


    def create_playlist(self, playlist_name):
        """Creates a playlist with a given name.
        
        Args:
            playlist_name: The playlist name.
        """

        playlists = self.video_playlist.playlist
        
        if playlist_name.lower() in playlists:
            print("Cannot create playlist: A playlist with the same name already exists")
        else:
            self.video_playlist.create_playlist(playlist_name)
            print(f"Successfully created new playlist: {playlist_name}")


    def add_to_playlist(self, playlist_name, video_id):
        """Adds a video to a playlist with a given name.
        
        Args:
            playlist_name: The playlist name.
            video_id: The video_id to be added.
        """

        playlists = self.video_playlist.playlist
        video = self.video_library.get_video(video_id)
        flagged = self.video_library.flagged
        
        if playlist_name.lower() not in playlists:
            print(f"Cannot add video to {playlist_name}: Playlist does not exist")
        elif video is None:
            print(f"Cannot add video to {playlist_name}: Video does not exist")
        elif video_id in flagged:
            print(f"Cannot add video to {playlist_name}: Video is currently flagged (reason: {flagged[video_id] if flagged[video_id] else 'Not supplied'})")
        elif video_id in playlists[playlist_name.lower()]["videos"]:
            print(f"Cannot add video to {playlist_name}: Video already added")
        else:
            self.video_playlist.add_to_playlist(playlist_name.lower(), video_id)
            print(f"Added video to {playlist_name}: {video.title}")


    def show_all_playlists(self):
        """Display all playlists."""

        playlists = list(self.video_playlist.playlist.values())
        playlists.sort(key=lambda x: x["name"])

        if len(playlists) <= 0:
            print("No playlists exist yet")
        else:
            print("Showing all playlists:")
            for playlist in playlists:
                print(playlist["name"])


    def show_playlist(self, playlist_name):
        """Display all videos in a playlist with a given name.
        
        Args:
            playlist_name: The playlist name.
        """
        playlists = self.video_playlist.playlist
        flagged = self.video_library.flagged

        if playlist_name.lower() not in playlists:
            print(f"Cannot show playlist {playlist_name}: Playlist does not exist")
        else:    
            print(f"Showing playlist: {playlist_name}")
            if len(playlists[playlist_name.lower()]["videos"]) <= 0:
                print("No videos here yet")
            else:
                for video_id in playlists[playlist_name.lower()]["videos"]:
                    video = self.video_library.get_video(video_id)
                    output = f" {video.title} ({video.video_id}) [{' '.join(video.tags)}]"
                    if video_id in flagged:
                        output = output + f" - FLAGGED (reason: {flagged[video_id] if flagged[video_id] else 'Not supplied'})"
                    print(output)


    def remove_from_playlist(self, playlist_name, video_id):
        """Removes a video to a playlist with a given name.
        
        Args:
            playlist_name: The playlist name.
            video_id: The video_id to be removed.
        """
        
        playlists = self.video_playlist.playlist
        video = self.video_library.get_video(video_id)
        
        if playlist_name.lower() not in playlists:
            print(f"Cannot remove video from {playlist_name}: Playlist does not exist")
        elif video is None:
            print(f"Cannot remove video from {playlist_name}: Video does not exist")
        elif video_id not in playlists[playlist_name.lower()]["videos"]:
            print(f"Cannot remove video from {playlist_name}: Video is not in playlist")
        else:
            self.video_playlist.remove_from_playlist(playlist_name.lower(), video_id)
            print(f"Removed video from {playlist_name}: {video.title}")


    def clear_playlist(self, playlist_name):
        """Removes all videos from a playlist with a given name.
        
        Args:
            playlist_name: The playlist name.
        """
        
        playlists = self.video_playlist.playlist

        if playlist_name.lower() not in playlists:
            print(f"Cannot clear playlist {playlist_name}: Playlist does not exist")
        else:
            self.video_playlist.clear_playlist(playlist_name.lower())
            print(f"Successfully removed all videos from {playlist_name}")


    def delete_playlist(self, playlist_name):
        """Deletes a playlist with a given name.
        
        Args:
            playlist_name: The playlist name.
        """
        
        playlists = self.video_playlist.playlist

        if playlist_name.lower() not in playlists:
            print(f"Cannot delete playlist {playlist_name}: Playlist does not exist")
        else:
            self.video_playlist.delete_playlist(playlist_name.lower())
            print(f"Deleted playlist: {playlist_name}")
    

    def search_videos(self, search_term):
        """Display all the videos whose titles contain the search_term.
        
        Args:
            search_term: The query to be used in search.
        """
        
        videos = list(filter(lambda x: (x.video_id not in self.video_library.flagged),self.video_library.get_all_videos()))
        videos.sort(key=lambda x: x.title)
        matched = []

        for video in videos:
            if search_term.strip().lower() in video.title.lower():
                matched.append(video)

        if len(matched) < 1:
            print(f"No search results for {search_term}")
        else:
            print(f"Here are the results for {search_term}:")
            for i, video in enumerate(matched):
                print(f"{i + 1}) {video.title} ({video.video_id}) [{' '.join(video.tags)}]")
            print("Would you like to play any of the above? If yes, specify the number of the video.")
            print("If your answer is not a valid number, we will assume it's a no.")
            try:
                x = int(input())
                if x < 1 or x > len(matched):
                    raise ValueError()
            except ValueError:
                return
            self.play_video(matched[int(x) - 1].video_id)
            

    def search_videos_tag(self, video_tag):
        """Display all videos whose tags contains the provided tag.
        
        Args:
            video_tag: The video tag to be used in search.
        """
        
        videos = list(filter(lambda x: (x.video_id not in self.video_library.flagged),self.video_library.get_all_videos()))
        videos.sort(key=lambda x: x.title)
        matched = []

        for video in videos:
            if video_tag.strip().lower() in video.tags:
                matched.append(video)

        if len(matched) < 1:
            print(f"No search results for {video_tag}")
        else:
            print(f"Here are the results for {video_tag}:")
            for i, video in enumerate(matched):
                print(f"{i + 1}) {video.title} ({video.video_id}) [{' '.join(video.tags)}]")
            print("Would you like to play any of the above? If yes, specify the number of the video.")
            print("If your answer is not a valid number, we will assume it's a no.")
            try:
                x = int(input())
                if x < 1 or x > len(matched):
                    raise ValueError()
            except ValueError:
                return
            self.play_video(matched[int(x) - 1].video_id)


    def flag_video(self, video_id, flag_reason=""):
        """Mark a video as flagged.
        
        Args:
            video_id: The video_id to be flagged.
            flag_reason: Reason for flagging the video.
        """
        
        video = self.video_library.get_video(video_id)
        flagged = self.video_library.flagged

        if video is None:
            print("Cannot flag video: Video does not exist")
        elif video_id in flagged:
            print("Cannot flag video: Video is already flagged")
        else:
            if self.current_video and self.current_video.video_id == video_id:
                self.stop_video()
            self.video_library.flag_video(video_id, flag_reason.strip())
            print(f"Successfully flagged video: {video.title} (reason: {flag_reason if flag_reason else 'Not supplied'})")


    def allow_video(self, video_id):
        """Removes a flag from a video.
        
        Args:
            video_id: The video_id to be allowed again.
        """

        video = self.video_library.get_video(video_id)
        flagged = self.video_library.flagged

        if video is None:
            print("Cannot remove flag from video: Video does not exist")
        elif video_id not in flagged:
            print("Cannot remove flag from video: Video is not flagged")
        else:
            self.video_library.unflag_video(video_id)
            print(f"Successfully removed flag from video: {video.title}")
