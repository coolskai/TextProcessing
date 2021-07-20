'''
1. 테스트를 위해 문자열 함수의 결과값을 str()함수를 통해 문자열로 변환
2. 결과값을 output 리스트에 추가함
3. 마지막에 한 번에 모두 출력(\n으로 하나씩 묶어) 
'''
output = []
sentence = 'Hello Python, This text is a sample.'
output.append(str('is' in sentence)) # 'is'가 있는가? bool 반환
output.append(str(sentence.index('This')))  # 'This'가 출현한 위치는?
output.append(str(sentence.split()))        # 공백문자 기준으로 단어 리스트 생성
output.append(str(sentence.split().index('This')))  #어단어리스트에서 'This'의 출현 위치
output.append(str(sentence.split()[3]))     # 단어리스트의 4번째 방에 있는 단어
output.append(str(sentence[-10:]))          # 뒤에서 10번째 문자부터 끝까지 문자열
output.append(str(sentence[::-1]))          # 처음부터 끝까지 문자열(뒤에서부터 하나씩)

print('\n'.join(output))