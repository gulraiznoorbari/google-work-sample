"""A video player class."""

from .video_library import VideoLibrary
import random

class VideoPlayer:
    """A class used to represent a Video Player."""

    def __init__(self):
        self._video_library = VideoLibrary()
        self.current_video = None
        self.isPlaying = False
        self.isPaused = False

    def number_of_videos(self):
        num_videos = len(self._video_library.get_all_videos())
        print(f"{num_videos} videos in the library")

    def show_all_videos(self):
        """Returns all videos."""
        videos = self._video_library.get_all_videos()
        videos.sort(key=lambda x: x.title)
        print("Here's a list of all available videos: ")
        for video in videos:
            tag = " ".join(video.tags)
            print(f" {video.title} ({video.video_id}) [{tag}]") 

    def play_video(self, video_id):
        """Plays the respective video.
        Args: video_id: The video_id to be played.
        """
        video = self._video_library.get_video(video_id)
        try:
            video.video_id
        except AttributeError:
            print("Cannot play video: Video does not exist")
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
        video = self._video_library.get_all_videos()
        number_of_videos = len(self._video_library.get_all_videos())
        if number_of_videos == 0:
            print("There are no videos available to play")
        else:
            if self.isPlaying is True:
                print(f"Stopping video: {self.current_video.title}")
                self.isPaused = False
            pick_video = random.choice(video)
            print(f"Playing video: {pick_video.title}")
            self.isPlaying = True
            self.current_video = pick_video

    def pause_video(self):
        """Pauses the current video."""
        video = self.current_video
        if video:
            if self.isPaused == True:
                print(f"Video already paused: {self.current_video.title}")
            elif self.isPaused == False:
                print(f"Pausing video: {self.current_video.title}")
                self.current_video = video
                self.isPaused = True
            else:
                print("Cannot pause video: No video is currently playing")


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
            if self.isPaused == False:
                print(f"Currently playing: {self.current_video.title} ({self.current_video.video_id}) [{tag}]")
            elif self.isPaused == True:
                print(f"Currently playing: {self.current_video.title} ({self.current_video.video_id}) [{tag}] - PAUSED")
            else:
                print("No video is currently playing")

    def create_playlist(self, playlist_name):
        """Creates a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        print("create_playlist needs implementation")

    def add_to_playlist(self, playlist_name, video_id):
        """Adds a video to a playlist with a given name.

        Args:
            playlist_name: The playlist name.
            video_id: The video_id to be added.
        """
        print("add_to_playlist needs implementation")

    def show_all_playlists(self):
        """Display all playlists."""

        print("show_all_playlists needs implementation")

    def show_playlist(self, playlist_name):
        """Display all videos in a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        print("show_playlist needs implementation")

    def remove_from_playlist(self, playlist_name, video_id):
        """Removes a video to a playlist with a given name.

        Args:
            playlist_name: The playlist name.
            video_id: The video_id to be removed.
        """
        print("remove_from_playlist needs implementation")

    def clear_playlist(self, playlist_name):
        """Removes all videos from a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        print("clears_playlist needs implementation")

    def delete_playlist(self, playlist_name):
        """Deletes a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        print("deletes_playlist needs implementation")

    def search_videos(self, search_term):
        """Display all the videos whose titles contain the search_term.

        Args:
            search_term: The query to be used in search.
        """
        print("search_videos needs implementation")

    def search_videos_tag(self, video_tag):
        """Display all videos whose tags contains the provided tag.

        Args:
            video_tag: The video tag to be used in search.
        """
        print("search_videos_tag needs implementation")

    def flag_video(self, video_id, flag_reason=""):
        """Mark a video as flagged.

        Args:
            video_id: The video_id to be flagged.
            flag_reason: Reason for flagging the video.
        """
        print("flag_video needs implementation")

    def allow_video(self, video_id):
        """Removes a flag from a video.

        Args:
            video_id: The video_id to be allowed again.
        """
        print("allow_video needs implementation")
