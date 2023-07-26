import pygame

class Fighter():
    def __init__(self, x, y, flip, data,sprite_sheet, sprite_frames):
        self.size = data[0]
        self.image_scale = data[1]
        self.offset = data[2]
        self.flip = flip
        self.sprite_list = self.load_sprites(sprite_sheet,sprite_frames)
        self.action = 0 # 0: idle|| 1: run || 2: jump || 3: atk1 || 4: atk2 || 5: hit || 6: death
        self.frame_index = 0
        self.image = self.sprite_list[self.action][self.frame_index]
        self.update_time = pygame.time.get_ticks()
        self.rect = pygame.Rect((x,y,80,180))
        self.vel_y =  0
        self.jump = False
        self.attacking = False
        self.attack_type = 0
        self.health = 100
    
    def load_sprites(self,sprite_sheet,sprite_frames):
        #extract images from spritesheet
        sprite_list = []
        for y, sprite in enumerate(sprite_frames):
            temp_img_lst = []
            for x in range(sprite):
                temp_img = sprite_sheet.subsurface(x * self.size, y * self.size, self.size, self.size)
                temp_img_lst.append(pygame.transform.scale(temp_img, (self.size * self.image_scale, self.size * self.image_scale)))
                sprite_list.append(temp_img_lst)  
        return sprite_list  
                 
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
            
        #ensure players are facing each other
        if target.rect.centerx > self.rect.centerx:
            self.flip = False
        else:
            self.flip = True
            
        #update player position
        self.rect.x += dx
        self.rect.y += dy
        
    #animation updates
    def update(self)
        
    def attack(self,surface,target):
        self.attacking = True
        hitbox = pygame.Rect(self.rect.centerx - (2 * self.rect.width * self.flip), self.rect.y, 2 * self.rect.width, self.rect.height)
        if hitbox.colliderect(target.rect):
            target.health -= 10
        
        pygame.draw.rect(surface, (0,255,0), hitbox)
        
    
    def draw(self,surface):
        img = pygame.transform.flip(self.image, self.flip, False)
        pygame.draw.rect(surface, (255,0,0), self.rect)
        surface.blit(img, (self.rect.x - (self.offset[0] * self.image_scale), self.rect.y - (self.offset[1] * self.image_scale)))