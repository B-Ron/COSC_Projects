import pygame

class Fighter():
    def __init__(self, player, x, y, flip, data, sprite_sheet, sprite_frames,sound):
        self.player= player
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
        self.running = False
        self.jump = False
        self.attacking = False
        self.attack_type = 0
        self.attack_cooldown = 0
        self.attack_sound = sound
        self.hit = False
        self.health = 100
        self.alive = True
    
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
                 
    def move(self, screen_width, screen_height, surface, target, round_over):
        SPEED = 10
        GRAVITY = 2
        dx = 0
        dy = 0
        self.running = False
        self.attack_type = 0
        
        #key presses
        key = pygame.key.get_pressed()
        
        
        #can only perfom actions if not attacking
        if self.attacking == False and self.alive == True and round_over == False:
            #check p1 controls
            if self.player == 1 :
             #movement
                if key[pygame.K_a]:
                    dx  = -SPEED
                    self.running = True
            
                if key[pygame.K_d]:
                    dx = SPEED
                    self.running = True
            
                #jumping
                if key[pygame.K_w] and self.jump == False:
                    self.vel_y = -30
                    self.jump = True
                #attack buttons
                if key[pygame.K_t] or key[pygame.K_y]:
                    self.attack(target)
                    #primary attack
                    if key[pygame.K_t]:
                        self.attack_type == 1
                
                    #secondary attack
                    if key[pygame.K_y]:
                        self.attack_type = 2
            
            #check p2 controls
            if self.player == 2: 
             #movement
                if key[pygame.K_LEFT]:
                    dx  = -SPEED
                    self.running = True
            
                if key[pygame.K_RIGHT]:
                    dx = SPEED
                    self.running = True
            
                #jumping
                if key[pygame.K_UP] and self.jump == False:
                    self.vel_y = -30
                    self.jump = True
                
                #attack buttons
                if key[pygame.K_KP1] or key[pygame.K_KP2]:
                    self.attack(target)
                    #primary attack
                    if key[pygame.K_KP1]:
                        self.attack_type == 1
                
                    #secondary attack
                    if key[pygame.K_KP2]:
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
        
        #attack cooldown
        if self.attack_cooldown > 0:
            self.attack_cooldown -= 1
            
        #update player position
        self.rect.x += dx
        self.rect.y += dy
        
    #animation updates
    def update(self):
        #check action player performs
        if self.health <= 0:
            self.health = 0
            self.alive = False
            self.update_action(6) # death
        
        elif self.hit == True:
            self.update_action(5) #hit
        
        elif self.attacking == True:
            if self.attack_type == 1:
                self.update_action(3) #atk1
            elif self.attack_type == 2:
                self.update_action(4) #atk2
                
        elif self.jump == True:
            self.update_action(2) # jump
        
        elif self.running == True:
            self.update_action(1) #run
        else:
            self.update_action(0) #idle
        
        cooldown = 50
        #update image
        self.image = self.sprite_list[self.action][self.frame_index]
        #check if time has passed since update
        if pygame.time.get_ticks() - self.update_time > cooldown:
            self.frame_index += 1
            self.update_time = pygame.time.get_ticks()
        #check if animation is finished
        if self.frame_index >= len(self.sprite_list[self.action]):
            #if player is dead, end animarion
            if self.alive == False:
                self.frame_index = len(self.sprite_list[self.action]) - 1
            else:
                self.frame_index = 0
                #check if attack is exe
                if self.action == 3 or self.action == 4:
                    self.attacking = False
                    self.attack_cooldown = 20
                #check if dmg was tanken
                if self.action == 5: #hit
                    self.hit == False
                    #if player was in middle of atk, stop atk
                    self.attacking = False
                    self.attack_cooldown = 20
        
    def attack(self,target):
        if self.attack_cooldown == 0:
            #exe atk
            self.attacking = True
            self.attack_sound.play()
            hitbox = pygame.Rect(self.rect.centerx - (2 * self.rect.width * self.flip), self.rect.y, 2 * self.rect.width, self.rect.height)
            if hitbox.colliderect(target.rect):
                target.health -= 10
                target.hit = True
        
    def update_action(self, new_action):
        #check if new action is different than previous
        if new_action != self.action:
            self.action = new_action
            #update animation
            self.frame_index = 0
            self.update_time = pygame.time.get_ticks()
    
    def draw(self,surface):
        img = pygame.transform.flip(self.image, self.flip, False)
        surface.blit(img, (self.rect.x - (self.offset[0] * self.image_scale), self.rect.y - (self.offset[1] * self.image_scale)))