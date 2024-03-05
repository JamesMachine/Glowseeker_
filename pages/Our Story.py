import streamlit as st

st.image("Nat_Profile.png", width=705)

our_story = '''
Welcome to Our Story! 🚀✨

Meet Natalie, the visionary founder of our exciting journey. 🌍 Hailing from the dynamic city of Hamburg, Germany, Natalie's story is one of passion, exploration, and a commitment to bringing innovation to the world of skincare. 💖

Originally from Germany, Natalie's adventure truly began when she embarked on a transformative year-long stay in Japan. 🇯🇵 This immersive experience not only deepened her appreciation for the beauty of Japanese culture but also sparked a keen interest in skincare rituals and traditions. 💆‍♀️✨

Upon her return to Hamburg, Natalie was determined to channel her newfound knowledge and passion into something extraordinary. The result? A startup company dedicated to revolutionizing the skincare industry. With a focus on blending the precision of German excellence with the grace of Japanese beauty practices, Natalie set out to create a skincare website and application that would redefine the way we care for our skin. 🌈💄

Central to our mission is the belief that skincare should be a personalized journey, guided by individual preferences and skin conditions. To bring this vision to life, Natalie sought the expertise of two talented data scientists. Their paths crossed at a startup event 🌐, where their shared passion for technology, innovation, and skincare sparked the beginning of a collaboration that would change the landscape of the industry. 🤝💼

Our application is more than just a skincare platform; it's a personalized guide fueled by a robust recommendation system. 📲💡 Tailored to your unique knowledge of ingredients and individual skin conditions, our technology is designed to empower you in making informed choices about your skincare routine. 🌺🌟

As we embark on this startup adventure, we invite you to join us in redefining skincare. Our commitment is to blend the best of Natalie's German roots, the wisdom gained from her time in Japan, and the expertise of our dedicated team. Together, we're creating a skincare experience that's as unique as you are. 🌟🌿

Welcome to the beginning of a beautiful journey – welcome to Our Story! 🎉✨

'''

st.markdown(f'<div style="text-align: justify;">{our_story}</div>', unsafe_allow_html=True)
