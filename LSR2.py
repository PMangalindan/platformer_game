


import pygame
from pygame.locals import*

##### classes

class Player1():
    
    def __init__(self, x, y):
        
        global platform_lst
        ###constants
        self.jump_speed = 7
        
        self.frame_counter = 2
        
        ### physics
        #gravity
        self.fall_acc = 2
        self.fall_speed = 0
        
        
        
        
        ### states    
        #
        self.hp       = 100
        self.energy   = 0
        self.run_speed = 10
        #
        self.facing   = 1        # 1 is right, -1 is left
        self.facing_y = 0
        self.jumpfall = 1        # 1 is in the air
        self.jump_limiter = 10
        self.jump_cooldown = 3
        self.just_fell = 1
        self.jump_delayer = 0
        self.max_fall_lenght_counter = 0
        #
        self.dash_cooldown = 0
        #
        self.slashing = 0        # not slashing
        self.firing   = 0        # not firing
        #
        self.platform_on = platform_lst[2]
        ### images
        self.images_run_r   = []
        self.runr_idx       = 0
        self.images_run_l   = []
        self.runl_idx       = 0
        self.run_anime_delayer = 0
        
        self.images_idle_r  = []
        self.idler_idx      = 0
        self.images_idle_l  = []
        self.idlel_idx      = 0
        self.idle_anime_delayer = 0
        
        self.images_brace   = []
        self.brace_idx      = 0
        
        self.images_vanish  = []
        self.vanish_idx     = 0
        
        self.images_vanish_l = []
        self.vanishl_idx     = 0
        
        self.images_appear  = []
        self.appear_idx     = 0
        
        self.images_slash_r = []
        self.slashr_idx     = 0
        self.images_slash_l = []
        self.slashl_idx     = 0
        self.images_slash_up = []
        self.images_slash_down = []
        
        self.images_charge = []
        self.charge_idx = 0
        
        self.images_dash = []
        self.dash_idx = 0
        
        self.slash_counter = 15
        self.slashing = 0
        self.slash_time_limit = 20
        
        
        self.run_speed_neg_cooldown = 0
        
        
        for num in range(10):
            img = pygame.image.load(r"eterminator_processed\run\sprint_0{}.png".format(num))
            
            
            img_right = pygame.transform.scale(img, (2*97, 2*108))
            self.images_run_r.append(img_right)
            img_left = pygame.transform.flip(img_right, True, False)
            self.images_run_l.append(img_left)
        
        for num in range(8):
            img = pygame.image.load("eterminator_processed\idle\idle_{}.png".format(num))
            img_idle = pygame.transform.scale(img, (2*97, 2*108))
            self.images_idle_r.append(img_idle)
            img_idle_l = pygame.transform.flip(img_idle, True, False)
            self.images_idle_l.append(img_idle_l)
            
        for num in range(18):
  
            img = pygame.image.load(r"eterminator_processed\attack\attack_{}.png".format(num)).convert_alpha()                
            img_a = pygame.transform.scale(img, (2*97, 2*108))
            self.images_brace.append(img_a)
           
        
        for num in range(13):
            
            if num < 10:  
                img = pygame.image.load(r"eterminator_processed\vanish\vanish_0{}.png".format(num)).convert_alpha() 
            else:
                img = pygame.image.load(r"eterminator_processed\vanish\vanish_{}.png".format(num)).convert_alpha() 
            img_v = pygame.transform.scale(img, (2*97, 2*108))
            self.images_vanish.append(img_v)
            
            img_van_l = pygame.transform.flip(img_v, True, False)
            self.images_vanish_l.append(img_van_l)
            
        for num in range(11):
            
            if num < 10:  
                img = pygame.image.load(r"eterminator_processed\appear\appear_0{}.png".format(num)).convert_alpha() 
            else:
                img = pygame.image.load(r"eterminator_processed\appear\appear_{}.png".format(num)).convert_alpha() 
            img_v = pygame.transform.scale(img, (2*97, 2*108))
            self.images_appear.append(img_v) 
            
            
        
        
        for num in range(5):
  
            img = pygame.image.load(r"eterminator_processed\slash\sprite_{}.png".format(num)).convert_alpha()                
            img_slash = pygame.transform.scale(img, (3*121, 3*70))
            self.images_slash_l.append(img_slash)
            
            img_slash_r = pygame.transform.flip(img_slash, True, False)
            self.images_slash_r.append(img_slash_r)
            
            img_down = pygame.transform.rotate(img_slash_r, -90)
            self.images_slash_down.append(img_down)
            
            img_up = pygame.transform.flip(img_down, False, True)
            self.images_slash_up.append(img_up)
            
        for num in range(6):
  
            img = pygame.image.load(r"eterminator_processed\charge\attack_{}.png".format(num)).convert_alpha()                
            img_a = pygame.transform.scale(img, (2*97, 2*108))
            self.images_charge.append(img_a)
            
            
        for num in range(6):
  
            img = pygame.image.load(r"eterminator_processed\dash2\sprite_{}.png".format(num)).convert_alpha()                
            img_a = pygame.transform.scale(img, (2*97, 2*108))
            self.images_dash.append(img_a)
            
            
        
        
        
        
        
        
        #initial position
        self.image = self.images_run_r[self.runr_idx]
        self.original_rect = self.image.get_rect()
        self.original_rect.x = x 
        self.original_rect.y = y
        
        
        self.slash_image = self.images_slash_r[0]
        self.slash_rect = self.slash_image.get_rect()
        
        self.slash_image_y = self.images_slash_up[0]
        self.slash_y_rect = self.slash_image_y.get_rect()
        
        
        
        
        
        self.current_rect = self.original_rect
        
        self.phantom_platform = pygame.Rect(0,0,0,0)
        
        
        
        # run rects
        self.rect_run_r = self.image.get_rect()
        self.rect_run_r.x = self.original_rect.x + 100
        self.rect_run_r.y = self.original_rect.y + 140
        self.rect_run_r.width = 40
        self.rect_run_r.height = 76
        
        
        self.rect_run_l = self.image.get_rect()
        self.rect_run_l.x = self.original_rect.x + 100 - self.rect_run_r.width - 6
        self.rect_run_l.y = self.original_rect.y + 140
        self.rect_run_l.width = 40
        self.rect_run_l.height = 76
        
        #idle rects
        self.rect_idle_r = self.image.get_rect()
        self.rect_idle_r.x = self.original_rect.x + 108
        self.rect_idle_r.y = self.original_rect.y + 120
        self.rect_idle_r.width = 30
        self.rect_idle_r.height = 96
        
        self.rect_idle_l = self.image.get_rect()
        self.rect_idle_l.x = self.original_rect.x + 108 - self.rect_idle_r.width - 20
        self.rect_idle_l.y = self.original_rect.y + 120
        self.rect_idle_l.width = 30
        self.rect_idle_l.height = 96
        
        #charge
        self.charge_rect = self.image.get_rect()
        self.charge_rect.x = self.original_rect.x + 110
        self.charge_rect.y = self.original_rect.y + 120
        self.charge_rect.width = 38
        self.charge_rect.height = 76
        
        #dash
        self.dash_rect = self.image.get_rect()
        self.dash_rect.y = self.original_rect.y + 140
        self.dash_rect.x = self.original_rect.x
        self.dash_rect.height = 76
        self.dash_rect.width = 160
        
        #
        self.pressed_key = 0
        
    
    def dash(self):
        
        self.dash_idx = 0
        temp_rect_y = self.original_rect.y + 0
        temp_rect_x = self.original_rect.x + 0
        if self.facing ==  1:
            
            while self.dash_idx < len(self.images_dash):
                
                screen.blit(bg, (0,0))
                clock.tick(20)
                
                self.image = self.images_dash[self.dash_idx]
                
                self.original_rect.y = temp_rect_y 
                self.original_rect.x = temp_rect_x + 80 + 40
                
                self.dash_rect.x = self.original_rect.x +40
                self.dash_rect.y = self.original_rect.y + 140
                
                for platform in platform_lst:
                    if platform.colliderect(self.dash_rect):
                        
                        self.original_rect.x = platform.x - self.original_rect.width
                        
                        
                
                
                #pygame.draw.rect(screen, "red", self.original_rect)
                #pygame.draw.rect(screen, "yellow", self.dash_rect)
            
                        

                screen.blit(self.image, self.original_rect) 
                platform_update()
                pygame.display.update()
                
                temp_rect2 = self.original_rect.y + 0

                self.dash_idx += 1
                
        elif self.facing ==  -1:
            
            while self.dash_idx < len(self.images_dash):
                
                screen.blit(bg, (0,0))
                clock.tick(20)
                
                self.image = pygame.transform.flip(self.images_dash[self.dash_idx], True, False)
                
                self.original_rect.y = temp_rect_y 
                self.original_rect.x = temp_rect_x  - 80 -40
                
                self.dash_rect.x = self.original_rect.x 
                self.dash_rect.y = self.original_rect.y + 140
                
                for platform in platform_lst:
                    if platform.colliderect(self.dash_rect):
                        
                        self.original_rect.x = platform.x + platform.width
                
                #pygame.draw.rect(screen, "red", self.original_rect)
                #pygame.draw.rect(screen, "yellow", self.dash_rect)
                
            
                        

                screen.blit(self.image, self.original_rect) 
                platform_update()
                pygame.display.update()
                
                temp_rect2 = self.original_rect.y + 0

                self.dash_idx += 1    
           
            
        self.image = self.images_run_r[0]
        self.original_rect.y = temp_rect2 
        if self.facing == 1:
            
            self.original_rect.x += 60
        elif self.facing == -1:
            self.original_rect.x -= 60
        #pygame.draw.rect(screen, "brown", self.original_rect)
        return
    
    def charge(self):
        self.charge_idx = 0
        
        if self.facing == 1:
            
            while self.charge_idx < len(self.images_charge):



                screen.blit(bg, (0,0))
                clock.tick(60)

                
                self.image = pygame.transform.flip(self.images_charge[self.charge_idx], True, False)
                self.charge_rect.x = self.original_rect.x + 83
                
                if self.charge_rect.x < self.platform_on.x:
                    self.original_rect.x = self.platform_on.x - 83
                    self.charge_rect.x = self.original_rect.x + 83
                
                
                #pygame.draw.rect(screen, "yellow", self.original_rect)
                #pygame.draw.rect(screen, "red", self.charge_rect)
                
                platform_update()        

                screen.blit(self.image, self.original_rect) 

                pygame.display.update()
                
                

                self.charge_idx += 1
                
        elif  self.facing == -1:  
            
            while self.charge_idx < len(self.images_charge):



                screen.blit(bg, (0,0))
                clock.tick(60)

                self.image = self.images_charge[self.charge_idx]
                
                self.charge_rect.x = self.original_rect.x + 73
                
                if self.charge_rect.x + self.charge_rect.width > self.platform_on.x + self.platform_on.width:
                    self.original_rect.x = self.platform_on.x + self.platform_on.width  - 73 - self.charge_rect.width
                    self.charge_rect.x = self.original_rect.x + 73
                    
                    
                
                #pygame.draw.rect(screen, "yellow", self.original_rect)
                #pygame.draw.rect(screen, "red", self.charge_rect)


                platform_update()        

                screen.blit(self.image, self.original_rect) 

                pygame.display.update()

                self.charge_idx += 1
            
            
            
        
    
    def slash(self):
        
        if self.slash_counter >= self.slash_time_limit:
            
            self.index_slash = 0
            slower = 5 
            
            if self.facing_y != 0:
                self.slash_y()
                return
            
            if self.facing == -1:

                while self.index_slash < len(self.images_slash_r):
                    screen.blit(bg, (0,0))
                    clock.tick(40)

                    slower += 1





                    self.image = self.images_vanish_l[self.index_slash]

                    self.slash_image = self.images_slash_l[self.index_slash]

                    self.index_slash += 1


                    self.slash_rect.x = (self.original_rect.x + self.original_rect.width) - self.slash_rect.width + 60
                    self.slash_rect.y = self.original_rect.y
                    #pygame.draw.rect(screen, "brown", self.slash_rect)
                    #pygame.draw.rect(screen, "blue", self.original_rect)



                    slower = 0 
                            

                    screen.blit(self.image, self.original_rect) 
                    screen.blit(self.slash_image, self.slash_rect)
                    platform_update()
                    pygame.display.update()


                self.slash_counter = 0

            elif self.facing == 1:

                self.index_slash = 0

                while self.index_slash < len(self.images_slash_r):
                    screen.blit(bg, (0,0))
                    clock.tick(40)





                    self.slashing = 1

                    self.image = self.images_vanish[self.index_slash]

                    self.slash_image = self.images_slash_r[self.index_slash]

                    self.index_slash += 1 

                    self.slash_rect.x = self.original_rect.x -60 
                    self.slash_rect.y = self.original_rect.y
                    #pygame.draw.rect(screen, "yellow", self.slash_rect)
                    #pygame.draw.rect(screen, "blue", self.original_rect)




                            

                    screen.blit(self.image, self.original_rect) 
                    screen.blit(self.slash_image, self.slash_rect)
                    platform_update()
                    pygame.display.update()



                    self.slashing = 0

                self.slash_counter = 0
            
        return 
    
    
    def slash_y(self):
        
        if self.facing_y == -1:
            
        
            while self.index_slash < len(self.images_slash_r):

                screen.blit(bg, (0,0))
                clock.tick(40)







                self.image = self.images_vanish_l[self.index_slash]

                self.slash_image_y = self.images_slash_down[self.index_slash]

                self.index_slash += 1


                self.slash_y_rect.x = self.current_rect.x + (self.current_rect.width/2 - 60)
                self.slash_y_rect.y = self.current_rect.y - 70

                #pygame.draw.rect(screen, "brown", self.slash_y_rect)
                #pygame.draw.rect(screen, "blue", self.original_rect)




                       

                screen.blit(self.image, self.original_rect) 
                screen.blit(self.slash_image_y, self.slash_y_rect)
                platform_update()
                pygame.display.update()


            self.slash_counter = 0
            
        elif self.facing_y == 1:

            while self.index_slash < len(self.images_slash_r):

                screen.blit(bg, (0,0))
                clock.tick(40)







                self.image = self.images_vanish[self.index_slash]

                self.slash_image_y = self.images_slash_up[self.index_slash]

                self.index_slash += 1


                self.slash_y_rect.x = self.current_rect.x + (self.current_rect.width/2 - 60)
                self.slash_y_rect.y = self.original_rect.y + self.original_rect.height - self.slash_y_rect.height + 70

                #pygame.draw.rect(screen, "brown", self.slash_y_rect)
                #pygame.draw.rect(screen, "blue", self.original_rect)




                        

                screen.blit(self.image, self.original_rect) 
                screen.blit(self.slash_image_y, self.slash_y_rect)
                platform_update()
                pygame.display.update()


            self.slash_counter = 0
        
        
        
    
    
    
    
    
    
    def gravity(self):
        
        self.fall_speed += self.fall_acc
        
        
        if self.fall_speed >= 40:        # limit fall speed
            self.fall_speed = 40
            self.max_fall_lenght_counter += 1
        else:
            self.max_fall_lenght_counter = 0
            
            
        self.original_rect.y += self.fall_speed
        
        self.rect_update()
        self.fall_collision_check(self.current_rect)
        
        
        
        
    
    def fall_collision_check(self, collision_rect):
        
        if self.jumpfall == 1:
            
            
            
            if self.fall_speed > 0  : # meaning falling
                
                #print(self.fall_speed)
                #print(self.current_rect.x + self.current_rect.width)
                #print(self.platform_on.x)
                
                
                
                
                    
                self.rect_update()
               
                
                
                for platform in platform_lst:
                    if platform.colliderect(collision_rect):
                        
                        self.platform_on = platform
                        #print((self.current_rect.y + self.current_rect.height) - platform.y )
                        if platform.y > self.current_rect.y + (self.current_rect.height - 41)  and (self.current_rect.x + self.current_rect.width) > platform.x and self.current_rect.x < (platform.x + platform.width):
                            
                            
                            
                            #print(str(platform) + "fell on this, collided")
                            if self.run_speed < 0:
                                
                                self.run_speed = (self.run_speed * -1)*2
                                
                            brace_lenght = self.fall_speed
                            self.just_fell = 0
                        
                            self.original_rect.y = platform.y - self.original_rect.height -1
                            self.rect_update()

                            self.jump_limiter = 0
                            
                            self.run_speed = 10
                            
                            self.slash_counter = self.slash_time_limit

                            self.fall_acc = 0
                            self.fall_speed = 0

                            self.jumpfall = 0
                            
                            self.dash_cooldown = 30

                            self.platform_on = platform
                            
                            
                                  
                            
                            #print(brace_lenght)
                            if brace_lenght >= 39 and self.max_fall_lenght_counter >= 7:
                                if self.facing == 1:
                                    
                                    i = 1
                                    slower = 5 
                                    while i < len(self.images_vanish) - 5:
                                        screen.blit(bg, (0,0))
                                        clock.tick(45)
                                        slower += 1

                                        if slower > 3:




                                            self.image = self.images_vanish[i]
                                            i += 1 



                                            slower = 0 

                                        screen.blit(self.image, self.original_rect)
                                        platform_update()                                                
                                        pygame.display.update()
                                else:
                                    
                                    i = 1
                                    slower = 5 
                                    while i < len(self.images_vanish_l) - 5:
                                        screen.blit(bg, (0,0))
                                        clock.tick(45)
                                        slower += 1

                                        if slower > 3:




                                            self.image = self.images_vanish_l[i]
                                            i += 1 



                                            slower = 0 

                                        screen.blit(self.image, self.original_rect)
                                        platform_update()                                                
                                        pygame.display.update()
                                    
                                    
                                    
                                #self.jump_delayer = 6
                                return
                            else:
                                
                                if self.facing == 1:
                                    i = 1
                                    slower = 5 
                                    while i < len(self.images_vanish) - 10:
                                        screen.blit(bg, (0,0))
                                        clock.tick(60)
                                        slower += 1

                                        if slower > 3:




                                            self.image = self.images_vanish[i]
                                            i += 1 



                                            slower = 0 
                                        screen.blit(self.image, self.original_rect)
                                        platform_update()                                                
                                        pygame.display.update()
                                        
                                else:
                                    i = 1
                                    slower = 5 
                                    while i < len(self.images_vanish_l) - 10:
                                        screen.blit(bg, (0,0))
                                        clock.tick(60)
                                        slower += 1

                                        if slower > 3:




                                            self.image = self.images_vanish_l[i]
                                            i += 1 



                                            slower = 0 
                                        screen.blit(self.image, self.original_rect)
                                        platform_update()                                                
                                        pygame.display.update()
                                    
                            
                                #self.jump_delayer = 4
                        
                else:
                    return
                
            elif self.fall_speed <= 0:  #rising   
                
                   
                
                
                
                for platform in platform_lst:
                    if platform.colliderect(collision_rect):
                        
                        if platform.y + platform.height - (self.current_rect.height/2) < self.current_rect.y   and (self.current_rect.x + self.current_rect.width) > platform.x and self.current_rect.x < (platform.x + platform.width):
                            
                            
                                    
                            self.original_rect.y = (platform.y  + platform.height) - (self.current_rect.y - self.original_rect.y) 
                                    


                            self.fall_speed = 0
                            self.jump_limiter = 10
                            self.fall_acc = 2

                            self.rect_update()
                            screen.blit(self.image, self.original_rect)    
                            platform_update()
                            
                        
        
            
    def rect_update(self):
        ### precise rects
        
        # run rects
        
        self.rect_run_r.x = self.original_rect.x + 100
        self.rect_run_r.y = self.original_rect.y + 140
        
        
        
        
        self.rect_run_l.x = self.original_rect.x + 100 - self.rect_run_r.width - 6
        self.rect_run_l.y = self.original_rect.y + 140
        
        
        #idle rects
        
        self.rect_idle_r.x = self.original_rect.x + 108
        self.rect_idle_r.y = self.original_rect.y + 120
        
        
        
        self.rect_idle_l.x = self.original_rect.x + 108 - self.rect_idle_r.width - 20
        self.rect_idle_l.y = self.original_rect.y + 120
        
        #charge rects
        
        self.charge_rect.x = self.original_rect.x + 73
        self.charge_rect.y = self.original_rect.y + 140
        
        
        
        
        
    def idle_anime(self):
        
        self.idle_anime_delayer += 1
        
        if self.facing == 1:
            
            self.rect_update()
            self.current_rect = self.rect_idle_r
            
            if self.idle_anime_delayer > 5:
            
                if self.idler_idx < len(self.images_idle_r):
                
                    self.image = self.images_idle_r[self.idler_idx]
                    self.rect_update()
                    
                    self.idler_idx += 1
                    self.idle_anime_delayer = 0
                else:
                    self.idler_idx = 0
                    self.idle_anime_delayer = 0
                    
        elif self.facing == -1:
            
            self.rect_update()
            self.current_rect = self.rect_idle_l
            
            if self.idle_anime_delayer > 5:
            
                if self.idlel_idx < len(self.images_idle_l):
                
                    self.image = self.images_idle_l[self.idlel_idx]
                    self.rect_update()
                
                    self.idlel_idx += 1
                    self.idle_anime_delayer = 0
                else:
                    self.idlel_idx = 0
                    self.idle_anime_delayer = 0            
        
    def run_right(self):
        
        self.run_anime_delayer += 1
        
        if self.facing == -1:   
            self.facing = 1
            
            
            
            self.original_rect.x -= 40     #aboutface gap
            
            
            self.rect_run_r.x = self.original_rect.x + 100
            self.rect_run_r.y = self.original_rect.y + 140
            
            
            self.current_rect = self.rect_run_r
            
            self.image = self.images_run_r[0]            
            
            #pygame.draw.rect(screen, "yellow", self._rect)
            
            
            
            
 
        
        
        
        elif self.facing == 1:
                    
            
            self.original_rect.x += self.run_speed            
            
            self.rect_run_r.x = self.original_rect.x + 100
            self.rect_run_r.y = self.original_rect.y + 140
            
            self.current_rect = self.rect_run_r
            
            if self.current_rect.x    > self.platform_on.x + self.platform_on.width + 45 : #fall
                
                
                
                self.platform_on = self.phantom_platform
                self.just_fell = 1
                self.fall_acc = 3
                
                
                
                self.jumpfall = 1
            
            self.rect_run_r.x = self.original_rect.x + 100
            self.rect_run_r.y = self.original_rect.y + 140                        
            self.fall_collision_check(self.rect_run_r)
            
            for platform in platform_lst:
                    if platform.colliderect(self.rect_run_r):
                        
                        
                        
                        if self.current_rect.x < platform.x  :
                            
                            if self.fall_speed < 0:                            #collision on air
                                self.run_speed = (self.run_speed * -1)/2
                                self.run_speed_neg_cooldown = 5
                                self.fall_speed = 0
                                
                                self.rect_run_r.x = self.original_rect.x + 100
                                self.rect_run_r.y = self.original_rect.y + 140
                                
                                self.current_rect = self.rect_run_r
                                
                                
                                
                            self.original_rect.x = platform.x - (self.current_rect.x + self.current_rect.width - self.original_rect.x)   ###   to calibrate
                            
                            self.rect_run_r.x = self.original_rect.x + 100
                            self.rect_run_r.y = self.original_rect.y + 140
                            
                            self.current_rect = self.rect_run_r
            
            
            if self.runr_idx < len(self.images_run_r):
                
                if self.run_anime_delayer > 2:
                    
                    self.image = self.images_run_r[self.runr_idx]
                    
                    

                    self.runr_idx += 1
                    
                    self.run_anime_delayer = 0
                    #pygame.draw.rect(screen, "yellow", self.original_rect)
        
                
                
                        
                
                
                
            else:
                self.runr_idx = 0
                
                      
                
                
                
    def run_left(self):
        self.run_anime_delayer += 1
        if self.facing == 1:   
            self.facing = -1
            self.original_rect.x += 40
            
            self.rect_idle_l.x = self.original_rect.x + 108 - self.rect_idle_r.width - 20
            self.rect_idle_l.y = self.original_rect.y + 120
            
            self.current_rect = self.rect_run_l
            
            
            self.image = self.images_run_l[0]
            #pygame.draw.rect(screen, "yellow", self.original_rect)
            
            
        
        
        
        elif self.facing == -1:
        
            self.original_rect.x -= self.run_speed            
            
            self.rect_idle_l.x = self.original_rect.x + 108 - self.rect_idle_r.width - 20
            self.rect_idle_l.y = self.original_rect.y + 120
            
            self.current_rect = self.rect_run_l
            #pygame.draw.rect(screen, "yellow", self.current_rect)
            
            if self.current_rect.x +  self.current_rect.width  < self.platform_on.x - 45:
                
                
                
                self.platform_on = self.phantom_platform
                self.just_fell = 1
                self.fall_acc = 3
                
                
                
                self.jumpfall = 1
                
            self.rect_run_l.x = self.original_rect.x + 100 - self.rect_run_r.width - 6
            self.rect_run_l.y = self.original_rect.y + 140
            self.fall_collision_check(self.rect_run_l)
            
            for platform in platform_lst:
                    if platform.colliderect(self.rect_run_l):
                        
                        
                        
                        
                        
                        if self.current_rect.x + self.current_rect.width > platform.x + platform.width : #
                            
                            
                            
                            if self.fall_speed < 0:
                                self.run_speed = (self.run_speed * -1)/2
                                self.run_speed_neg_cooldown = 5
                                self.fall_speed = 0
                                
                                
                                
                                
                                                                
                            
                            self.original_rect.x = platform.x + platform.width - (self.current_rect.x - self.original_rect.x)   ###   to calibrate
                            
                            self.rect_update
                            
                            self.current_rect = self.rect_run_l
                        
                        
            if self.runl_idx < len(self.images_run_l):
                
                if self.run_anime_delayer > 2:
                    
                    self.image = self.images_run_l[self.runl_idx]
                    

                    self.runl_idx += 1
                    
                    self.run_anime_delayer = 0
                    #pygame.draw.rect(screen, "yellow", self.original_rect)
                                
            else:
                self.runl_idx = 0   
                
        
                
    def jump(self):
        
        
        if self.just_fell == 0:
            
                


            if self.jump_limiter < 5:
                  




                self.jumpfall = 1
                self.jump_cooldown += 1

                if self.jump_cooldown > 2:

                    screen.blit(self.image, self.original_rect)     
                    if self.jump_limiter < 5:





                        self.fall_acc = 2
                        self.fall_speed -= self.jump_speed
                        
                        self.run_speed = 13
                        self.jump_limiter += 1

                        self.just_fell = 0
                        self.fall_state = 1 
                        
                        self.dash_cooldown = 30

                        




                        #pygame.draw.rect(screen, "yellow", player_rect)








                    else:

                        self.jump_limiter = 0

                        self.fall_acc = 2

                        self.jump_cooldown = 0

                        self.jumpfall = 1           

                        

                        
        
        
        
        
        
    def update(self):
        key = pygame.key.get_pressed()
        
        self.pressed_key = 0
        
        
        
        self.rect_update()
        
        if key[pygame.K_i]:
            
            if self.jumpfall == 0:
                self.charge()
                return
        
        if key[pygame.K_l]:
            if self.dash_cooldown >= 30:
                
                self.dash()
                self.dash_cooldown = 0
                self.max_fall_lenght_counter = 0
                
        
        
        if key[pygame.K_k]:  #JUMP
            
            #if self.frame_counter % 2 != 0:
            if self.jump_delayer == 0:
                self.jump()
            else:
                self.jump_delayer -= 1
                
        
        
        
        
        
        if key[pygame.K_d]: # RUN RIGHT
            
            #if self.frame_counter % 2 == 0:
            if self.pressed_key == 0:
            
                self.fall_collision_check(self.rect_run_r)
                self.rect_update()
                self.run_right()
                self.rect_update()
                
                self.pressed_key = 1 
            
            
            
        if key[pygame.K_a]: # RUN LEFT
            
            #if self.frame_counter % 2 == 0:
            if self.pressed_key == 0:
                
                self.fall_collision_check(self.rect_run_l)
                self.rect_update()
                self.run_left()
                self.rect_update()
                
                self.pressed_key = -1
        if key[pygame.K_s]: #looking down
            if self.jumpfall == 1:
                
                self.facing_y = -1
        
        
        if key[pygame.K_w]: # looking up
            
            self.facing_y = 1
            
            
            
        if key[pygame.K_a] == False and  key[pygame.K_d] == False:
            
            self.rect_update()
            if self.facing == -1: #looking left
                
                self.rect_idle_l.x = self.original_rect.x + 108 - self.rect_idle_r.width - 20
                self.rect_idle_l.y = self.original_rect.y + 120
                
                self.current_rect = self.rect_idle_l
                
                if self.current_rect.x + self.current_rect.width/2 >= self.platform_on.x + self.platform_on.width and self.jumpfall == 0:
                    self.original_rect.x = self.original_rect.x - self.current_rect.width/2
                    self.rect_update()
                #pygame.draw.rect(screen, "yellow", self.current_rect)
                
                
                
                
            elif self.facing == 1: #looking right
                
                
                self.rect_idle_r.x = self.original_rect.x + 108
                self.rect_idle_r.y = self.original_rect.y + 120
                
                self.current_rect = self.rect_idle_r
                
                if self.current_rect.x + self.current_rect.width/2 <= self.platform_on.x and self.jumpfall == 0:
                    self.original_rect.x = self.original_rect.x + self.current_rect.width/2
                    self.rect_update()
                #pygame.draw.rect(screen, "yellow", self.original_rect)
                #pygame.draw.rect(screen, "red", self.current_rect)
                    
                    
                
                
                
                
                
                
                
            
            if self.jumpfall == 0:
                #
                
                #if self.facing == 1:
                    
                    #if self.current_rect.x + self.current_rect.width/2 > self.platform_on.x + self.platform_on.width:
                        
                        #self.original_rect.x = (self.platform_on.x + self.platform_on.width) - (self.current_rect.width/2) - 108 
                        #pygame.draw.rect(screen, "yellow", self.original_rect)
                        #pygame.draw.rect(screen, "violet", self.current_rect)
                #   
                    
                if self.current_rect.x + self.current_rect.width   < self.platform_on.x :


                    #print("FALLING#############################")
                    #print(self.current_rect.x + self.current_rect.width)
                    #print(self.platform_on.x)

                    #pygame.draw.rect(screen, "yellow", self.current_rect)

                    self.platform_on = self.phantom_platform
                    self.just_fell = 1
                    self.fall_acc = 2
                    self.rect_update()

                    self.jumpfall = 1
                    

                elif self.current_rect.x  > self.platform_on.x + self.platform_on.width :


                    #print("FALLING#############################")
                    #print(self.current_rect.x + self.current_rect.width)
                    #print(self.platform_on.x)

                    #pygame.draw.rect(screen, "yellow", self.current_rect)

                    self.platform_on = self.phantom_platform
                    self.just_fell = 1
                    self.fall_acc = 2
                    self.rect_update()

                    self.jumpfall = 1    
                
            self.idle_anime()
            
            
        if key[pygame.K_j]:
            self.slash()
            
        
        
            
        
            
            
                
        self.rect_update() #temp
                
         
        
        
        
        
        #screen.blit(self.image, self.original_rect)
        #platform_update()
        
        
        
            
        if self.jump_cooldown < 3:
            self.jump_cooldown += 1
        
        if self.dash_cooldown < 30:
            self.dash_cooldown += 1
            
        if self.run_speed < 0:
            if self.run_speed_neg_cooldown == 0:
                self.run_speed = 2*(self.run_speed* -1)
            else:
                self.run_speed_neg_cooldown -= 1
                
        if self.slash_counter <= self.slash_time_limit:
            
            self.slash_counter += 1
        
        self.facing_y = 0
        self.gravity()
        
        #self.frame_counter += 1
        
        #pygame.draw.rect(screen, "grey", self.current_rect)        
        screen.blit(self.image, self.original_rect) 
        
        platform_update() 
        pygame.display.update()
        
        
        
##### functions

##platform updater

def platform_update():
        
    global platform_lst
    p_lst = platform_lst
    
    i = 0
    while i != len(p_lst):
        
        pygame.draw.rect(screen, "grey", p_lst[i])
        i += 1
    
    
    
    







    

###############################################################
pygame.init()  

screen_w = 1238 
screen_h = 700

clock = pygame.time.Clock()
fps = 60
screen = pygame.display.set_mode((screen_w, screen_h))



pygame.display.set_caption("Lonely Sad Robot")
#load imgs
bg = pygame.image.load("bg4.jpg")
#load music

music = pygame.mixer.music.load("music\LBYP- Black Sheep.mp3")
pygame.mixer.music.play(-1)

platform_lst = [pygame.Rect(700, 590, 150, 75),
                pygame.Rect(0, 0, 75, 700),
                pygame.Rect(1238 - 75, 0, 75, 700),
                pygame.Rect(0, 665,1238, 75),
                pygame.Rect(850, 400, 150, 45),
                pygame.Rect(525, 330, 150, 45),]

player1 = Player1(50,50)

####  430



run = True
while run:
    clock.tick(fps)
    screen.blit(bg, (0,0))
    
    
    
    
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            
      
    platform_update() 
    player1.update()
    pygame.display.update()
    
    
    
       
        
        
    



    
    


pygame.quit()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




