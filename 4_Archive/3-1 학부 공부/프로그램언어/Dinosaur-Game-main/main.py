import pygame
import sys
import random

# Pygame 초기화
pygame.init()

# 화면 설정
screen = pygame.display.set_mode((1280, 720))  # 게임 창 크기 설정
clock = pygame.time.Clock()  # 프레임 속도 제어를 위한 시계
pygame.display.set_caption("Dino Game")  # 창 제목 설정

# 폰트 설정
game_font = pygame.font.Font("assets/PressStart2P-Regular.ttf", 24)  # 폰트와 크기 설정

# 클래스
class Cloud(pygame.sprite.Sprite):  # 구름 관리 클래스
    def __init__(self, image, x_pos, y_pos):
        super().__init__()
        self.image = image  # 구름 이미지
        self.x_pos = x_pos  # 구름의 초기 x 위치
        self.y_pos = y_pos  # 구름의 초기 y 위치
        self.rect = self.image.get_rect(center=(self.x_pos, self.y_pos))  # 구름의 위치와 크기 설정

    def update(self):  # 구름 이동 로직
        self.rect.x -= 1  # 구름이 왼쪽으로 이동


class Dino(pygame.sprite.Sprite):  # 플레이어 캐릭터(공룡) 클래스
    def __init__(self, x_pos, y_pos):
        super().__init__()
        # 달리는 애니메이션 스프라이트
        self.running_sprites = [
            pygame.transform.scale(pygame.image.load("assets/Dino1.png"), (80, 100)),
            pygame.transform.scale(pygame.image.load("assets/Dino2.png"), (80, 100))
        ]

        # 숙이는 애니메이션 스프라이트
        self.ducking_sprites = [
            pygame.transform.scale(pygame.image.load(f"assets/DinoDucking1.png"), (110, 60)),
            pygame.transform.scale(pygame.image.load(f"assets/DinoDucking2.png"), (110, 60))
        ]

        self.x_pos = x_pos  # 공룡의 초기 x 위치
        self.y_pos = y_pos  # 공룡의 초기 y 위치
        self.current_image = 0  # 현재 애니메이션 프레임
        self.image = self.running_sprites[self.current_image]  # 초기 애니메이션 설정
        self.rect = self.image.get_rect(center=(self.x_pos, self.y_pos))  # 공룡의 위치와 크기 설정
        self.velocity = 50  # 점프 속도
        self.gravity = 3.0  # 중력 효과
        self.ducking = False  # 공룡이 숙이고 있는지 여부

    def jump(self):  # 점프 동작
        jump_sfx.play()  # 점프 소리 재생
        if self.rect.centery >= 600:  # 지면에 있는 경우에만 점프 가능
            while self.rect.centery - self.velocity > 260:  # 일정 높이까지 상승
                self.rect.centery -= 1

    def duck(self):  # 숙이는 동작
        self.ducking = True
        self.rect.centery = 625  # 공룡의 y 위치를 조정하여 숙인 상태로 만듦

    def unduck(self):  # 숙인 상태 해제
        self.ducking = False
        self.rect.centery = 600  # 공룡을 원래 위치로 복구

    def apply_gravity(self):  # 중력 효과 적용
        if self.rect.centery <= 600:  # 지면 위에 있을 때 아래로 떨어짐
            self.rect.centery += self.gravity

    def update(self):  # 캐릭터의 업데이트 로직
        self.animate()  # 애니메이션 업데이트
        self.apply_gravity()  # 중력 적용

    def animate(self):  # 애니메이션 프레임 전환
        self.current_image += 0.05  # 프레임을 부드럽게 전환
        if self.current_image >= 2:  # 애니메이션 순환
            self.current_image = 0
        self.image = self.ducking_sprites[int(self.current_image)] if self.ducking else self.running_sprites[int(self.current_image)]


class Cactus(pygame.sprite.Sprite):  # 장애물(선인장) 클래스
    def __init__(self, x_pos, y_pos):
        super().__init__()
        self.x_pos = x_pos  # 선인장의 초기 x 위치
        self.y_pos = y_pos  # 선인장의 초기 y 위치
        self.sprites = [
            pygame.transform.scale(pygame.image.load(f"assets/cacti/cactus{i}.png"), (100, 100))
            for i in range(1, 7)
        ]  # 다양한 선인장 스프라이트 로드
        self.image = random.choice(self.sprites)  # 랜덤으로 선인장 선택
        self.rect = self.image.get_rect(center=(self.x_pos, self.y_pos))  # 위치와 크기 설정

    def update(self):  # 선인장 이동 로직
        self.x_pos -= game_speed  # 왼쪽으로 이동
        self.rect = self.image.get_rect(center=(self.x_pos, self.y_pos))  # 위치 업데이트


class Ptero(pygame.sprite.Sprite):  # 장애물(익룡) 클래스
    def __init__(self):
        super().__init__()
        self.x_pos = 1300  # 익룡의 초기 x 위치
        self.y_pos = random.choice([280+240, 295+240, 350+240])  # 익룡의 랜덤 y 위치
        self.sprites = [
            pygame.transform.scale(pygame.image.load("assets/Ptero1.png"), (84, 62)),
            pygame.transform.scale(pygame.image.load("assets/Ptero2.png"), (84, 62))
        ]  # 익룡 스프라이트 로드
        self.current_image = 0  # 현재 애니메이션 프레임
        self.image = self.sprites[self.current_image]  # 초기 이미지 설정
        self.rect = self.image.get_rect(center=(self.x_pos, self.y_pos))  # 위치와 크기 설정

    def update(self):  # 익룡 업데이트 로직
        self.animate()  # 애니메이션 업데이트
        self.x_pos -= game_speed  # 왼쪽으로 이동
        self.rect = self.image.get_rect(center=(self.x_pos, self.y_pos))  # 위치 업데이트

    def animate(self):  # 애니메이션 전환
        self.current_image += 0.025  # 프레임 변경 속도
        if self.current_image >= 2:  # 애니메이션 순환
            self.current_image = 0
        self.image = self.sprites[int(self.current_image)]

# Variables
game_speed = 5  # 게임 진행 속도
jump_count = 10  # 점프 횟수 (미사용)
player_score = 0  # 플레이어 점수
game_over = False  # 게임 오버 여부
obstacle_timer = 0  # 장애물 생성 타이머
obstacle_spawn = False  # 장애물 생성 플래그
obstacle_cooldown = 1000  # 장애물 생성 간격(ms)

# Surfaces
ground = pygame.image.load("assets/ground.png")  # 지면 이미지 로드
ground = pygame.transform.scale(ground, (1280, 20))  # 크기 조정
ground_x = 0  # 지면의 초기 x 위치
ground_rect = ground.get_rect(center=(640, 600))  # 지면 위치 설정
cloud = pygame.image.load("assets/cloud.png")  # 구름 이미지 로드
cloud = pygame.transform.scale(cloud, (200, 80))  # 크기 조정

# Groups
cloud_group = pygame.sprite.Group()  # 구름 그룹
obstacle_group = pygame.sprite.Group()  # 장애물 그룹
dino_group = pygame.sprite.GroupSingle()  # 공룡 그룹
ptero_group = pygame.sprite.Group()  # 익룡 그룹

# Objects
dinosaur = Dino(50, 600)  # 공룡 객체 생성
dino_group.add(dinosaur)  # 공룡을 그룹에 추가

# Sounds
death_sfx = pygame.mixer.Sound("assets/sfx/lose.mp3")  # 게임 오버 사운드
points_sfx = pygame.mixer.Sound("assets/sfx/100points.mp3")  # 점수 사운드
jump_sfx = pygame.mixer.Sound("assets/sfx/jump.mp3")  # 점프 사운드

# Events
CLOUD_EVENT = pygame.USEREVENT  # 사용자 정의 이벤트 (구름 생성)
pygame.time.set_timer(CLOUD_EVENT, 3000)  # 3초마다 구름 생성

# Functions
def end_game():  # 게임 종료 처리 함수
    global player_score, game_speed
    game_over_text = game_font.render("Game Over!", True, "black")  # 게임 오버 텍스트
    game_over_rect = game_over_text.get_rect(center=(640, 300))
    score_text = game_font.render(f"Score: {int(player_score)}", True, "black")  # 점수 텍스트
    score_rect = score_text.get_rect(center=(640, 340))
    screen.blit(game_over_text, game_over_rect)
    screen.blit(score_text, score_rect)
    game_speed = 5  # 게임 속도 초기화
    cloud_group.empty()  # 구름 제거
    obstacle_group.empty()  # 장애물 제거

# 게임 루프
while True:
    keys = pygame.key.get_pressed()  # 키 입력 확인
    if keys[pygame.K_DOWN]:  # 아래 키 눌림
        dinosaur.duck()  # 공룡 숙임
    else:
        if dinosaur.ducking:  # 숙인 상태였다면
            dinosaur.unduck()  # 숙임 해제

    for event in pygame.event.get():  # 이벤트 처리
        if event.type == pygame.QUIT:  # 창 닫기 이벤트
            pygame.quit()
            sys.exit()
        if event.type == CLOUD_EVENT:  # 구름 생성 이벤트
            current_cloud_y = random.randint(50, 300)  # 랜덤 y 위치 설정
            current_cloud = Cloud(cloud, 1380, current_cloud_y)  # 구름 객체 생성
            cloud_group.add(current_cloud)  # 구름 그룹에 추가
        if event.type == pygame.KEYDOWN:  # 키 다운 이벤트
            if event.key == pygame.K_SPACE or event.key == pygame.K_UP:  # 스페이스바나 위 키 눌림
                dinosaur.jump()  # 공룡 점프
                if game_over:  # 게임 오버 상태라면 초기화
                    game_over = False
                    game_speed = 5
                    player_score = 0

    screen.fill("white")  # 화면 흰색으로 초기화

    # 충돌 처리
    if pygame.sprite.spritecollide(dino_group.sprite, obstacle_group, False):  # 공룡과 장애물 충돌 여부 확인
        game_over = True  # 게임 오버 상태로 전환
        death_sfx.play()  # 게임 오버 사운드 재생
    if game_over:  # 게임 오버 상태일 경우
        end_game()  # 종료 화면 표시

    if not game_over:  # 게임 진행 중일 경우
        game_speed += 0.0025  # 게임 속도 증가
        if round(player_score, 1) % 100 == 0 and int(player_score) > 0:  # 점수가 100의 배수일 때
            points_sfx.play()  # 점수 사운드 재생

        # 장애물 생성 타이밍 확인
        if pygame.time.get_ticks() - obstacle_timer >= obstacle_cooldown:
            obstacle_spawn = True

        if obstacle_spawn:  # 장애물 생성 플래그가 참일 경우
            obstacle_random = random.randint(1, 50)  # 랜덤 값으로 장애물 결정
            if obstacle_random in range(1, 7):  # 선인장 생성
                new_obstacle = Cactus(1280, 590)
                obstacle_group.add(new_obstacle)
                obstacle_timer = pygame.time.get_ticks()
                obstacle_spawn = False
            elif obstacle_random in range(7, 10):  # 익룡 생성
                new_obstacle = Ptero()
                obstacle_group.add(new_obstacle)
                obstacle_timer = pygame.time.get_ticks()
                obstacle_spawn = False

        player_score += 0.1  # 점수 증가
        player_score_surface = game_font.render(str(int(player_score)), True, ("black"))  # 점수 표시
        screen.blit(player_score_surface, (1150, 10))

        # 그룹 업데이트 및 화면에 그리기
        cloud_group.update()
        cloud_group.draw(screen)

        ptero_group.update()
        ptero_group.draw(screen)

        dino_group.update()
        dino_group.draw(screen)

        obstacle_group.update()
        obstacle_group.draw(screen)

        # 지면 이동
        ground_x -= game_speed  # 지면 이동
        screen.blit(ground, (ground_x, 600))  # 지면 표시
        screen.blit(ground, (ground_x + 1280, 600))  # 두 번째 지면 표시 (순환)

        if ground_x <= -1280:  # 지면이 화면 왼쪽으로 완전히 나가면
            ground_x = 0  # 위치 초기화

    clock.tick(120)  # 초당 120프레임으로 실행
    pygame.display.update()  # 화면 업데이트
