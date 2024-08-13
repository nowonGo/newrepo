import streamlit as st

# 제목
st.title('😎 나의 MBTI 특성 알아보기 🎉')

# 사용자 이름 입력
name = st.text_input('이름을 입력해주세요 🙋')

# MBTI 유형 선택
mbti = st.selectbox('당신의 MBTI를 선택해주세요! 🤔', 
                    ['INTJ', 'INTP', 'ENTJ', 'ENTP', 
                     'INFJ', 'INFP', 'ENFJ', 'ENFP', 
                     'ISTJ', 'ISFJ', 'ESTJ', 'ESFJ', 
                     'ISTP', 'ISFP', 'ESTP', 'ESFP'])

# 버튼을 눌렀을 때 결과 출력
if st.button('결과 보기 🔍'):
    if name and mbti:
        # MBTI 특성 설명
        if mbti == 'INTJ':
            description = '🤖 전략적 사고와 독립성을 중요시하는 당신! 계획적이고 목표지향적이에요. 미래지향적인 사고를 통해 늘 큰 그림을 그리죠! 📈'
            best_match = 'ENFP 🧠'
            worst_match = 'ESFP 🎉'
        elif mbti == 'INFP':
            description = '🎨 당신은 이상주의자! 감성적이며 깊은 내면을 가지고 있어요. 사람들에게 진심을 다하며, 공감을 중요시해요. 💖'
            best_match = 'ENTJ 👔'
            worst_match = 'ESTP 🚀'
        elif mbti == 'ENTP':
            description = '💡 당신은 창의적이고 논쟁을 즐기는 타입! 호기심이 많고 새로운 아이디어에 열려 있어요. 항상 새로운 도전을 추구하죠! 🏆'
            best_match = 'INFJ 🌟'
            worst_match = 'ISFJ 🛡️'
        # 다른 MBTI 유형들에 대한 설명 추가 가능
        else:
            description = '🛠️ 아직 입력된 정보가 없네요! 다른 유형을 선택해보세요.'

        # 결과 출력
        st.write(f'🌟 {name}님의 MBTI 유형은 {mbti}입니다!')
        st.write(description)
        st.write(f'🔥 당신과 가장 잘 맞는 유형은 {best_match}입니다!')
        st.write(f'🚫 당신과 가장 맞지 않는 유형은 {worst_match}입니다.')
    else:
        st.write('이름과 MBTI를 모두 입력해주세요! 🤗')
