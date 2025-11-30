# pygame 및 필요한 모듈 임포트
import pygame, sys, random

# Pygame 초기화
pygame.init()

# 화면의 가로, 세로 크기 설정
WIDTH, HEIGHT = 1280, 720

# 점수와 텍스트를 표시하기 위한 폰트 설정
FONT = pygame.font.SysFont("Consolas", int(WIDTH/20))

# Pygame 화면 생성
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pong!")  # 게임 창 제목 설정

# 프레임 조절을 위한 시계 생성
CLOCK = pygame.time.Clock()

# 플레이어 패들 설정
player = pygame.Rect(0, 0, 10, 100)  # 패들의 크기 및 초기 위치
player.center = (WIDTH-100, HEIGHT/2)  # 오른쪽 중앙에 위치

# 상대방 패들 설정
opponent = pygame.Rect(0, 0, 10, 100)
opponent.center = (100, HEIGHT/2)  # 왼쪽 중앙에 위치

# 점수 초기화
player_score, opponent_score = 0, 0

# 공 리스트 초기화
balls = []

# 공 설정 (초기 공 2개)
for i in range(2):
    ball = pygame.Rect(0, 0, 20, 20)  # 공의 크기 및 초기 위치
    ball.center = (WIDTH/2, HEIGHT/2)  # 화면 중앙에 위치
    x_speed, y_speed = random.choice([1, -1]) * random.randint(8, 12), random.choice([1, -1]) * random.randint(8, 12) # 공의 방향 및 속도 랜덤 결정
    balls.append({'rect': ball, 'x_speed': x_speed, 'y_speed': y_speed})

# 게임 리셋 함수
def reset_game():
    global player_score, opponent_score, balls
    player_score, opponent_score = 0, 0
    balls = []
    for i in range(2):
        ball = pygame.Rect(0, 0, 20, 20)
        ball.center = (WIDTH/2, HEIGHT/2)
        x_speed, y_speed = random.choice([1, -1]) * random.randint(8, 12), random.choice([1, -1]) * random.randint(8, 12)
        balls.append({'rect': ball, 'x_speed': x_speed, 'y_speed': y_speed})

# 게임 루프 시작
while True:
    # 키 입력 상태 확인
    keys_pressed = pygame.key.get_pressed()

    # 플레이어 패들 위로 이동
    if keys_pressed[pygame.K_UP]:
        if player.top > 0:  # 화면 위쪽 경계를 넘지 않도록 제한
            player.top -= 10

    # 플레이어 패들 아래로 이동
    if keys_pressed[pygame.K_DOWN]:
        if player.bottom < HEIGHT:  # 화면 아래쪽 경계를 넘지 않도록 제한
            player.bottom += 10

    # 이벤트 처리 (예: 창 닫기)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()  # Pygame 종료
            sys.exit()  # 프로그램 종료

        # 게임 오버 후 아무 키나 누르면 게임 초기화
        if event.type == pygame.KEYDOWN and (player_score == 10 or opponent_score == 10):
            reset_game()

    # 공 이동
    if player_score < 10 and opponent_score < 10:
        for b in balls:
            b['rect'].x += b['x_speed'] * 0.8
            b['rect'].y += b['y_speed'] * 0.8

            # 공이 화면의 위쪽이나 아래쪽에 닿을 경우 방향 반전
            if b['rect'].bottom >= HEIGHT or b['rect'].top <= 0:
                b['y_speed'] = -b['y_speed']

            # 공이 화면 왼쪽에 닿을 경우 플레이어 점수 증가 및 공 리셋
            if b['rect'].left <= 0:
                player_score += 1
                b['rect'].center = (WIDTH / 2, HEIGHT / 2)
                b['x_speed'], b['y_speed'] = random.choice([1, -1]) * random.randint(8, 12), random.choice([1, -1]) * random.randint(8, 12)

            # 공이 화면 오른쪽에 닿을 경우 상대방 점수 증가 및 공 리셋
            if b['rect'].right >= WIDTH:
                opponent_score += 1
                b['rect'].center = (WIDTH / 2, HEIGHT / 2)
                b['x_speed'], b['y_speed'] = random.choice([1, -1]) * random.randint(8, 12), random.choice([1, -1]) * random.randint(8, 12)

            # 공이 플레이어 패들에 닿으면 방향 반전
            if b['rect'].colliderect(player):
                b['x_speed'] = -b['x_speed']

            # 공이 상대방 패들에 닿으면 방향 반전
            if b['rect'].colliderect(opponent):
                b['x_speed'] = -b['x_speed']
        
    # 점수를 화면에 표시할 텍스트 렌더링
    player_score_text = FONT.render(str(player_score), True, "white")
    opponent_score_text = FONT.render(str(opponent_score), True, "white")

    # 상대방 패들 AI 동작 (가장 가까운 공의 위치에 따라 이동)
    if player_score < 10 and opponent_score < 10:
        nearest_ball = min(balls, key=lambda b: abs(b['rect'].centerx - opponent.centerx))
        if opponent.y < nearest_ball['rect'].y:
            opponent.top += 7
        if opponent.bottom > nearest_ball['rect'].y:
            opponent.bottom -= 7

    # 화면을 검은색으로 채우기
    SCREEN.fill("Black")

    # 플레이어 패들, 상대방 패들, 공을 그리기
    if player_score < 10 and opponent_score < 10:
        pygame.draw.rect(SCREEN, "white", player)
        pygame.draw.rect(SCREEN, "white", opponent)
        for b in balls:
            pygame.draw.circle(SCREEN, "white", b['rect'].center, 10)
        

    # 점수를 화면에 표시
    SCREEN.blit(player_score_text, (WIDTH/2+50, 50))
    SCREEN.blit(opponent_score_text, (WIDTH/2-50, 50))

    # 게임 오버 시 메시지 표시
    if player_score == 10 or opponent_score == 10:
        game_over_text = FONT.render("Game over!", True, "white")
        SCREEN.blit(game_over_text, (WIDTH/2 - game_over_text.get_width()/2, HEIGHT/2))
    
    # 화면 업데이트
    pygame.display.update()

    # 프레임 속도 제한 (60 FPS)
    CLOCK.tick(60)