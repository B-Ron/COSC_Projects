import pygame

class Fighter():
    def __init__(self,x,y):
        self.rect = pygame.Rect((x,y,80,180))
        self.vel_y =  0
        self.jump = False
        self.attacking = False
        self.attack_type = 0
        self.health = 100
        
    def move(self, screen_width, screen_height, surface, target):
        SPEED = 10
        GRAVITY = 2
        dx = 0
        dy = 0
        
        #key presses
        key = pygame.key.get_pressed()
        
        
        #can only perfom actions if not attacking
        if self.attacking == False:
             #movement
            if key[pygame.K_a]:
                dx  = -SPEED
        
            if key[pygame.K_d]:
                dx = SPEED
        
            #jumping
            if key[pygame.K_w]and self.jump == False:
                self.vel_y = -30
                self.jump = True
            #attack buttons
            if key[pygame.K_t] or key[pygame.K_y]:
                self.attack(surface,target)
                #primary attack
                if key[pygame.K_t]:
                    self.attack_type == 1
            
                #secondary attack
                if key[pygame.K_y]:
                    self.attack_type = 2
        
        #apply gravity
        self.vel_y += GRAVITY
            
        dy += self.vel_y   
        
        #map endpoints
        if self.rect.left + dx < 0:
            dx =  -self.rect.left
        if self.rect.right + dx > screen_width:
            dx = screen_width - self.rect.right
        if self.rect.bottom + dy > screen_height - 110:
            self.jump = False
            self.vel_y = 0
            dy = screen_height - 110 - self.rect.bottom
            
            
        #update player position
        self.rect.x += dx
        self.rect.y += dy
        
    def attack(self,surface,target):
        self.attacking  = True
        hitbox = pygame.Rect(self.rect.centerx, self.rect.y, 2 * self.rect.width, self.rect.height)
        if hitbox.colliderect(target.rect):
            target.health -= 10
        
        pygame.draw.rect(surface, (0,255,0), hitbox)
        
    
    def draw(self,surface):
        pygame.draw.rect(surface, (255,0,0), self.rect)