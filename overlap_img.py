def pair_n_overlap(images):
    new_images = []
    for i in range(0, len(images)-1, 2):
        src = cv2.imread(images[i], cv2.IMREAD_COLOR)
        try : 
            src = src.astype('uint8')
        except AttributeError:
            print(src)
            print(f"AttributeError occurred on {i}th img")
            continue
        if i == len(images)-1: #last img deleted(has no img to pair)
            None 
        else: #pairing
            dst = cv2.imread(images[i+1], cv2.IMREAD_COLOR)
            try : 
                dst = dst.astype('uint8')
            except AttributeError:
                print(dst)
                print("AttributeError occurred")
                continue
            #print(src,dst)
            new_images.append(cv2.addWeighted(src, 0.5, dst, 0.5, 0.0))
            

    return new_images

def overlap(images):
    new_images = []
    for i in range(0, len(images)-1, 2):
        src = images[i]
        if i == len(images)-1: #last img deleted(has no img to pair)
            None 
        else: #pairing
            dst = images[i+1]
            new_images.append(cv2.addWeighted(src, 0.5, dst, 0.5, 0.0))
            
    return new_images
