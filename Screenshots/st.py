import streamlit as st
import streamlit_webrtc as webrtc

def main():
    
    audio_stream = webrtc.AudioProcessor(
        constraints={
            "audio": True,
        },
        media_stream_constraints={
            "video": False,
            "audio": True,
        },
    )
    webrtc_ctx = webrtc.StreamlitWebRTC(
        src_audio=audio_stream,
        width=0,
        height=0,
        key="audio",
    )
    st.write("You said: ", audio_stream.value)

if __name__ == "__main__":
    main()
