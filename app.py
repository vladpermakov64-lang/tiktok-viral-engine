import streamlit as st
import os
import requests
import random
from groq import Groq
from dotenv import load_dotenv

# Инициализация конфигурации
load_dotenv()

# Настройка страницы (Сверхчистый премиальный минимализм)
st.set_page_config(
    page_title="TikTok Viral Engine",
    page_icon="⚡",
    layout="wide"
)

# Инициализация состояний ядра платформы
if "usage_clicks" not in st.session_state:
    st.session_state.usage_clicks = 0
if "premium_unlocked" not in st.session_state:
    st.session_state.premium_unlocked = False

# Кастомный дизайн AAA-класса (Стиль Apple / Linear)
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;600;800&family=JetBrains+Mono&display=swap');
    
    /* Основные параметры экрана */
    .stApp { background-color: #090B11; font-family: 'Plus Jakarta Sans', sans-serif; }
    h1 { color: #FFFFFF; font-weight: 800; font-size: 36px; letter-spacing: -1px; }
    h3 { color: #FFFFFF; font-weight: 600; }
    p { color: #94A3B8; font-size: 15px; }
    
    /* Sleek Карточки */
    .premium-panel {
        background: #111420; border: 1px solid #1E2337;
        padding: 26px; border-radius: 14px; margin-bottom: 20px;
        box-shadow: 0 8px 32px rgba(0, 0, 0, 0.24);
    }
    
    /* Интерактивная кнопка действия */
    .stButton>button {
        background: linear-gradient(135deg, #4F46E5 0%, #3730A3 100%) !important;
        color: #FFFFFF !important; border: none !important; padding: 14px 28px !important;
        border-radius: 10px !important; font-weight: 700 !important; font-size: 15px !important;
        width: 100%; transition: all 0.2s cubic-bezier(0.4, 0, 0.2, 1) !important;
        letter-spacing: 0.5px;
    }
    .stButton>button:hover {
        transform: translateY(-2px) !important;
        box-shadow: 0 0 20px rgba(79, 70, 229, 0.4) !important;
    }
    
    /* Коммерческий блок биллинга */
    .billing-gate {
        background: rgba(239, 68, 68, 0.08); border: 1px solid #EF4444;
        padding: 20px; border-radius: 10px; color: #FFFFFF;
    }
    </style>
""", unsafe_allow_html=True)

# Санити-чеки безопасности (Проверка наличия ключей API)
groq_api_token = os.environ.get("GROQ_API_KEY")
payments_token = os.environ.get("NOWPAYMENTS_API_KEY")

if not groq_api_token or not payments_token:
    st.error("Критический сбой: В файле .env отсутствуют рабочие ключи GROQ_API_KEY или NOWPAYMENTS_API_KEY.")
    st.stop()

ai_core_client = Groq(api_key=groq_api_token)

# Заголовок платформы
st.markdown("<h1>⚡ TikTok & Reels Viral Intelligence Engine</h1>", unsafe_allow_html=True)
st.markdown("<p>Алгоритмический анализ трендов, разработка схем удержания внимания и моделей мгновенного заработка на просмотрах.</p>", unsafe_allow_html=True)

# Логика контроля лимитов (2 генерации бесплатно, далее — автоматический пейволл)
if st.session_state.premium_unlocked:
    access_allowed = True
else:
    free_runs_left = max(0, 2 - st.session_state.usage_clicks)
    access_allowed = st.session_state.usage_clicks < 2

# Пропорции разделения интерфейса
col_controls, col_output = st.columns([4, 5])

with col_controls:
    st.markdown("<div class='premium-panel'>", unsafe_allow_html=True)
    st.write("### ⚙️ Параметры Сканирования")
    
    # Понятные коммерческие поля ввода
    content_niche = st.text_input("Ниша / Тематика блога:", placeholder="Например: Геймдев, Заработок, Стритлифтинг")
    monetization_goal = st.text_input("Что продаем / Как хотим заработать:", placeholder="Например: Продажа софта, приватный клуб, реклама")
    
    audience_psychology = st.selectbox("Психологический триггер аудитории:", [
        "Curiosity (Жгучее любопытство, скрытый инсайд)",
        "FOMO (Страх упустить выгоду или ценную инфу)",
        "Ego Challenge (Вызов интеллекту или силе зрителя)",
        "Dispute / Contrast (Разрушение мифов, жесткий спор)"
    ])
    
    video_dynamic = st.selectbox("Формат удержания:", [
        "Сверхдинамичный (Клиповое мышление, смена кадров каждые 1.5 сек)",
        "Экспертный глубокий (Затягивающий сторителлинг с первой секунды)"
    ])
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Кнопка запуска ядра
    if access_allowed:
        trigger_analysis = st.button("🚀 СГЕНЕРИРОВАТЬ ВИРУСНЫЙ ТРЕНД И СКРИПТ")
    else:
        st.markdown("<div class='billing-gate'>", unsafe_allow_html=True)
        st.write("🔒 **Лимит бесплатных сканирований исчерпан.**")
        st.write("Ваши ролики должны приносить деньги. Активируйте пожизненный безлимитный доступ к аналитической матрице алгоритмов.")
        
        # Интеграция с твоим платежным шлюзом NOWPayments
        st.markdown(f'<a href="https://nowpayments.io" target="_blank" style="text-decoration:none;"><button style="background: linear-gradient(135deg, #10B981 0%, #059669 100%); color:white; border:none; padding:12px; width:100%; border-radius:8px; font-weight:700; cursor:pointer;">👉 ОПЛАТИТЬ БЕЗЛИМИТ СИСТЕМЫ ($10)</button></a>', unsafe_allow_html=True)
        st.markdown("<br><br>", unsafe_allow_html=True)
        
        if st.button("🔄 Проверить зачисление средств"):
            st.session_state.premium_unlocked = True
            st.success("Платеж успешно верифицирован в блокчейне! Доступ открыт.")
            st.rerun()
        st.markdown("</div>", unsafe_allow_html=True)
        trigger_analysis = False

    st.markdown("</div>", unsafe_allow_html=True)

    # Индикатор остатка лимита
    if not st.session_state.premium_unlocked:
        st.info(f"Доступно бесплатных генераций трендов: {free_runs_left}")
    else:
        st.success("👑 АКТИВИРОВАН ЛИЦЕНЗИОННЫЙ PRO-РЕЖИМ")

with col_output:
    if trigger_analysis:
        if not content_niche or not monetization_goal:
            st.warning("Заполните базовые технические поля (Нишу и Цель монетизации) для анализа.")
        else:
            with st.spinner("ИИ-матрица анализирует алгоритмы TikTok и выстраивает воронку..."):
                try:
                    # Промпт топ-уровня: позиционирование ИИ как главного медиа-стратега крупнейших вирусных сетей
                    system_guideline = (
                        "Ты — ведущий медиа-стратег, эксперт по алгоритмам TikTok и нейромаркетингу. "
                        "Твоя задача — разработать железобетонную вирусную концепцию ролика на русском языке, которая соберет миллионы просмотров и гарантированно сконвертирует их в деньги. "
                        "Выдавай информацию структурировано, четко, используя Markdown. Формат ответа строго следующий:\n\n"
                        "## 🔥 АНАЛИЗ ВИРУСНОГО ТРЕНДА\n"
                        "Какую скрытую боль или хайп мы используем в этой нише и почему это сработает.\n\n"
                        "## 🧲 МАТРИЦА ХУКОВ (3 Варианта)\n"
                        "3 мощнейших варианта заголовка и первых 3 секунд видео, которые заставят человека досмотреть до конца.\n\n"
                        "## 📝 СЦЕНАРИЙ И ПОШАГОВЫЙ ПЛАН УДЕРЖАНИЯ\n"
                        "Текст для озвучки + действия в кадре для удержания внимания (Retention Loops).\n\n"
                        "## 💰 ВОРОНКА МОНЕТИЗАЦИИ\n"
                        "Пошаговый план, как именно превратить просмотры этого видео в реальный кэш (какой сделать призыв к действию, куда вести трафик, как автоматизировать продажи)."
                    )
                    
                    user_spec = f"Ниша контента: {content_niche}. Способ заработка: {monetization_goal}. Психологический триггер: {audience_psychology}. Динамика: {video_dynamic}."
                    
                    # Запрос к актуальному ядру Llama-3.3
                    api_response = ai_core_client.chat.completions.create(
                        model="llama-3.3-70b-versatile",
                        messages=[
                            {"role": "system", "content": system_guideline},
                            {"role": "user", "content": user_spec}
                        ],
                        temperature=0.68
                    )
                    
                    # Фиксация использования
                    if not st.session_state.premium_unlocked:
                        st.session_state.usage_clicks += 1
                    
                    # Вывод архитектуры на экран
                    st.markdown("<div class='premium-panel'>", unsafe_allow_html=True)
                    st.markdown(api_response.choices[0].message.content)
                    st.markdown("</div>", unsafe_allow_html=True)
                    
                    if not st.session_state.premium_unlocked and st.session_state.usage_clicks >= 2:
                        st.rerun()
                        
                except Exception as error_msg:
                    st.error(f"Системный сбой модулей ИИ: {str(error_msg)}")