import streamlit as st
from streamlit_player import st_player, _SUPPORTED_EVENTS
#st.set_page_config(layout='wide')

st.title('The Music Masters Fan Page')

st.markdown("""
**The Music Masters** 
* [Twitter](https://twitter.com/themusicmaster9)
* [Instagram](https://www.instagram.com/themusicmasters.official/)            
            
            
""")

# set the sidebar
st.sidebar.header('User control options')
progressInterval = st.sidebar.text_input('interval',1000)
volumenumber = st.sidebar.slider("Volume", 0.0, 1.0, 1.0, .01)
loopflag = st.sidebar.checkbox("Loop", True)
playflag = st.sidebar.checkbox("Playing", True)
muteflag = st.sidebar.checkbox("Muted", True)


playlist = {'New released playlist':'https://youtu.be/rWHoBQ7Dj3c','Mini cover playlist':'https://youtube.com/playlist?list=PLAGhjTyfdowjpaGIO1e3ipOWyxK8b_Zli'} 
urls = st.multiselect('Choose the playlists you want to play', list(playlist.keys()), 'New released playlist')

for url in urls :
    playlist_url = st.text_input('Playlist URL', playlist[url])
    st_player(playlist_url,loop=loopflag, playing = playflag, muted = muteflag, volume = volumenumber, progress_interval = int(progressInterval), key =url)


# Help document
# streamlit_player.st_player(url, height=None, playing=None, loop=None, controls=True, light=None, volume=None, muted=None, playback_rate=None, progress_interval=None, play_inline=None, events=None, config=None, key=None)
# Embed a video or music player.

# Parameters
# ----------
# url : str
#     The url of a video or song to play.
# height : int or None 
#     Set player height.
# playing : bool or None
#     Set to true or false to pause or play the media.
# loop : bool or None
#     Set to true or false to loop the media. 
# controls : bool
#     Set to true or false to display native player controls.
#     For Vimeo videos, hiding controls must be enabled by the video owner.
# light : bool or None
#     Set to true to show just the video thumbnail, which loads the full player on click.
# volume : int or None
#     Set the volume of the player, between 0 and 1.
#     None sets default volume on all players.
# muted : bool or None
#     Mutes the player. Only works if volume is set.
# playback_rate : int or None
#     Set the playback rate of the player.
#     Only supported by YouTube, Wistia, and file paths.
# progress_interval : int or None
#     The time between onProgress callbacks, in milliseconds.
# play_inline : bool or None
#     Applies the playsinline attribute where supported.
# events : [str] or None
#     Events streamlit will receive feedbacks from.
#     `onReady`, `onEnablePIP` and `onDisablePIP` are not supported.
#     More information at https://github.com/cookpete/react-player#callback-props
# config : dict or None
#     Override options for the various players.
#     More information at https://github.com/cookpete/react-player#config-prop
# key : str or None
#     An optional string to use as the unique key for the widget.
#     If this is omitted, a key will be generated for the widget
#     based on its content. Multiple widgets of the same type may
#     not share the same key.