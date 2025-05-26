import pyautogui
import keyboard

# ตั้งค่าพื้นฐาน
click_button = 'left'   # ปุ่มคลิก: 'left', 'right', 'middle'
start_stop_key = 's'    # กดเพื่อเริ่ม/หยุดคลิก
exit_key = 'esc'        # กดเพื่อออกจากโปรแกรม

clicking = False  # สถานะคลิก

print("📌 AutoClick พร้อมทำงานแล้ว (โหมดไม่พัก)")
print(f"➡️  กด '{start_stop_key}' เพื่อเริ่ม/หยุดคลิก")
print(f"❌ กด '{exit_key}' เพื่อออกจากโปรแกรม")

while True:
    try:
        if keyboard.is_pressed(start_stop_key):
            clicking = not clicking
            print("🟢 เริ่มคลิก" if clicking else "⛔️ หยุดคลิก")
            while keyboard.is_pressed(start_stop_key):
                pass  # รอก่อนปล่อยปุ่ม เพื่อป้องกันกดซ้ำ

        while clicking:
            if keyboard.is_pressed(exit_key):
                print("👋 ออกจากโปรแกรมแล้ว")
                raise SystemExit
            pyautogui.click(button=click_button)

        if keyboard.is_pressed(exit_key):
            print("👋 ออกจากโปรแกรมแล้ว")
            break

    except:
        break
