"""A video playlist class."""

class Playlist:
    
    """A class used to represent a Playlist."""
    def __init__(self):
        self.playlist = {}

    def create_playlist(self, playlist_name):
        """Creates a new playlist 
        
        Args:
            playlist_name: The playlist name.
        """
        self.playlist[playlist_name.lower()] = {"name": playlist_name, "videos": []}

    def add_to_playlist(self, playlist_name, video_id):
        """Add video to an existing playlist
        
        Args:
            playlist_name: The playlist name
            video_id: The video_id to be added
        """
        self.playlist[playlist_name.lower()]["videos"].append(video_id)

    def remove_from_playlist(self, playlist_name, video_id):
        """Remove video from playlist
        
        Args:
            playlist_name: The playlist name
            video_id: The video_id to be removed
        """
        self.playlist[playlist_name.lower()]["videos"].remove(video_id)

    def clear_playlist(self, playlist_name):
        """Removes all videos from a playlist
        
        Args:
            playlist_name: The playlist name
        """
        self.playlist[playlist_name.lower()]["videos"].clear()

    def delete_playlist(self, playlist_name):
        """Deletes the playlist with a given name
        
        Args:
            playlist_name: The name of playlist
        """
        self.playlist.pop(playlist_name)

        