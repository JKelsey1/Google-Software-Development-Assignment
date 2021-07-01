"""A video player class."""

from .video_library import VideoLibrary
is_playing = False
is_paused = False
previous_video = None
now_playing = None

class VideoPlayer:
    """A class used to represent a Video Player."""

    def __init__(self):
        self._video_library = VideoLibrary()

    def number_of_videos(self):
        num_videos = len(self._video_library.get_all_videos())
        print(f"{num_videos} videos in the library")

    def show_all_videos(self):
        """Returns all videos."""
        all_videos = self._video_library.get_all_videos()
        all_videos.sort(key=lambda x: x.title)
        print("Here is a list of all available videos:")

        for video in all_videos:
            tagString = str(video.tags)
            print(video.title, "(", video.video_id, ")", "[", tagString.strip("()"), "]")

    def play_video(self, video_id):
        global is_playing
        global previous_video
        global now_playing
        global is_paused

        now_playing = self._video_library.get_video(video_id)

        if not now_playing:
            print(f"Cannot play video: Video does not exist")
        else:
            if is_playing is True:
                print(f"Stopping video: {previous_video}")
                print(f"Playing video: {now_playing.title}")
                is_paused = False
                previous_video = now_playing.title
            else:
                print(f"Playing video: {now_playing.title}")
                is_playing = True
                is_paused = False
                old_video = now_playing.title

    def stop_video(self):
        global is_playing
        global previous_video
        global now_playing
        """Stops the current video."""

        if is_playing:
            print(f"Stopping video: {now_playing.title}")
            is_playing = False
            previous_video = None
        else:
            if not is_playing:
                print("Cannot stop video: No video is currently playing.")
                previous_video = None

    def play_random_video(self):
        """Plays a random video from the video library."""

        print("play_random_video needs implementation")

    def pause_video(self):
        """Pauses the current video."""

        print("pause_video needs implementation")

    def continue_video(self):
        """Resumes playing the current video."""

        print("continue_video needs implementation")

    def show_playing(self):
        """Displays video currently playing."""

        print("show_playing needs implementation")

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
