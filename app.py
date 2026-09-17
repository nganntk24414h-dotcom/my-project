import streamlit as st
from pathlib import Path

# =========================================================
# 1. CẤU HÌNH TRANG
# =========================================================

st.set_page_config(
    page_title="FinTech WDI Story",
    page_icon="📊",
    layout="wide"
)

# Thư mục chứa app.py
BASE_DIR = Path(__file__).parent


# =========================================================
# 2. HÀM HIỂN THỊ ẢNH AN TOÀN
# =========================================================

def show_image(filename, caption=None):
    """
    Hiển thị ảnh nằm cùng thư mục với app.py.
    Nếu không tìm thấy ảnh thì báo lỗi nhẹ thay vì làm app bị crash.
    """
    image_path = BASE_DIR / filename

    if image_path.exists():
        st.image(
            str(image_path),
            caption=caption,
            use_container_width=True
        )
    else:
        st.warning(f"Không tìm thấy file ảnh: {filename}")


# =========================================================
# 3. CSS - GIAO DIỆN DẠNG BÀI BÁO
# =========================================================

st.markdown(
    """
    <style>

    .block-container {
        max-width: 1150px;
        padding-top: 3rem;
        padding-bottom: 5rem;
    }

    .hero-label {
        font-size: 0.9rem;
        font-weight: 700;
        letter-spacing: 0.12em;
        text-transform: uppercase;
        color: #7d8590;
        margin-bottom: 1rem;
    }

    .hero-title {
        font-size: 3.2rem;
        line-height: 1.12;
        font-weight: 800;
        margin-bottom: 1.2rem;
    }

    .hero-subtitle {
        font-size: 1.25rem;
        line-height: 1.7;
        color: #aeb6c1;
        max-width: 900px;
        margin-bottom: 2rem;
    }

    .section-label {
        font-size: 0.85rem;
        font-weight: 700;
        letter-spacing: 0.1em;
        text-transform: uppercase;
        color: #7d8590;
        margin-top: 2rem;
        margin-bottom: 0.5rem;
    }

    .section-title {
        font-size: 2.35rem;
        line-height: 1.2;
        font-weight: 800;
        margin-bottom: 1rem;
    }

    .article-text {
        font-size: 1.1rem;
        line-height: 1.8;
        margin-bottom: 1.2rem;
    }

    .insight {
        padding: 1.2rem 1.4rem;
        border-left: 4px solid #4c8bf5;
        background: rgba(76, 139, 245, 0.08);
        border-radius: 6px;
        margin-top: 1.2rem;
        margin-bottom: 2rem;
        font-size: 1.05rem;
        line-height: 1.7;
    }

    .question {
        padding: 1.2rem 1.4rem;
        border-radius: 8px;
        background: rgba(255, 255, 255, 0.05);
        margin: 1.2rem 0 2rem 0;
        font-size: 1.15rem;
        line-height: 1.7;
    }

    hr {
        margin-top: 3rem;
        margin-bottom: 3rem;
    }

    </style>
    """,
    unsafe_allow_html=True
)


# =========================================================
# 4. HERO - MỞ ĐẦU
# =========================================================

st.markdown(
    '<div class="hero-label">World Bank WDI · FinTech Data Story</div>',
    unsafe_allow_html=True
)

st.markdown(
    """
    <div class="hero-title">
        Số hóa có thực sự giúp tài chính trở nên dễ tiếp cận hơn?
    </div>
    """,
    unsafe_allow_html=True
)

st.markdown(
    """
    <div class="hero-subtitle">
        Một câu chuyện dữ liệu về Việt Nam, Thái Lan và Singapore:
        từ kết nối Internet, khả năng tiếp cận tài chính đến câu hỏi
        liệu sự mở rộng tài chính số có thực sự mang lại lợi ích đồng đều.
    </div>
    """,
    unsafe_allow_html=True
)

st.markdown("---")


# =========================================================
# 5. PHẦN 1 - INTERNET
# =========================================================

st.markdown(
    '<div class="section-label">Phần 1 · Cuộc rượt đuổi số hóa</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="section-title">Việt Nam đang thu hẹp khoảng cách Internet</div>',
    unsafe_allow_html=True
)

st.markdown(
    """
    <div class="article-text">
        Giai đoạn 2010–2024 cho thấy ba quốc gia có quỹ đạo số hóa khác nhau.
        Việt Nam chưa dẫn đầu về tỷ lệ sử dụng Internet, nhưng tốc độ hội tụ
        với Thái Lan là điểm đáng chú ý.
    </div>
    """,
    unsafe_allow_html=True
)

show_image(
    "image4.png",
    "Tăng trưởng GDP bình quân đầu người và tỷ lệ dân số sử dụng Internet"
)

st.markdown(
    """
    <div class="insight">
        <b>Điểm đáng chú ý:</b>
        Việt Nam tăng từ khoảng 31% dân số sử dụng Internet năm 2010
        lên khoảng 84% năm 2024. Trong cùng giai đoạn, Thái Lan vượt 90%,
        còn Singapore duy trì mức rất cao và tiến gần trạng thái bão hòa.
    </div>
    """,
    unsafe_allow_html=True
)

st.markdown(
    """
    <div class="question">
        <b>Câu hỏi tiếp theo:</b><br>
        Kết nối Internet tăng nhanh, nhưng điều đó có thực sự đi cùng
        với việc nhiều người hơn được tham gia vào hệ thống tài chính?
    </div>
    """,
    unsafe_allow_html=True
)

st.markdown("---")


# =========================================================
# 6. PHẦN 2 - ACCOUNT OWNERSHIP & GINI
# =========================================================

st.markdown(
    '<div class="section-label">Phần 2 · Từ kết nối đến tài chính</div>',
    unsafe_allow_html=True
)

st.markdown(
    """
    <div class="section-title">
        Nhiều người có tài khoản hơn, nhưng bất bình đẳng không tự động giảm
    </div>
    """,
    unsafe_allow_html=True
)

st.markdown(
    """
    <div class="article-text">
        Theo kỳ vọng của tài chính toàn diện, khả năng tiếp cận dịch vụ
        tài chính tốt hơn có thể đi cùng với kết quả phân phối thu nhập tốt hơn.
        Tuy nhiên, dữ liệu của ba quốc gia cho thấy mối quan hệ này không đơn giản.
    </div>
    """,
    unsafe_allow_html=True
)

show_image(
    "image3.png",
    "Mối liên hệ giữa tỷ lệ sở hữu tài khoản và hệ số Gini"
)

st.markdown(
    """
    <div class="insight">
        <b>Nghịch lý đáng chú ý:</b>
        tỷ lệ sở hữu tài khoản có thể rất cao nhưng mức bất bình đẳng
        thu nhập vẫn không thấp. Vì vậy, mở rộng khả năng tiếp cận tài chính
        chưa đủ để kết luận rằng lợi ích kinh tế được phân phối đồng đều.
    </div>
    """,
    unsafe_allow_html=True
)

st.markdown(
    """
    <div class="article-text">
        Việt Nam có tỷ lệ sở hữu tài khoản tăng đáng kể,
        nhưng sự cải thiện về bất bình đẳng không diễn ra tương ứng.
        Thái Lan có tỷ lệ sở hữu tài khoản cao hơn,
        trong khi Singapore cho thấy rõ rằng mức độ tiếp cận tài chính rất cao
        không đồng nghĩa với hệ số Gini thấp.
    </div>
    """,
    unsafe_allow_html=True
)

st.markdown("---")


# =========================================================
# 7. PHẦN 3 - GINI
# =========================================================

st.markdown(
    '<div class="section-label">Phần 3 · Bất bình đẳng thu nhập</div>',
    unsafe_allow_html=True
)

st.markdown(
    """
    <div class="section-title">
        Bất bình đẳng có giảm, nhưng tốc độ cải thiện rất khác nhau
    </div>
    """,
    unsafe_allow_html=True
)

show_image(
    "image2.png",
    "Thay đổi hệ số Gini từ đầu kỳ đến cuối kỳ"
)

st.markdown(
    """
    <div class="article-text">
        Cả ba quốc gia đều cho thấy xu hướng cải thiện về Gini trong
        phép so sánh đầu kỳ – cuối kỳ của báo cáo, nhưng mức độ thay đổi khác nhau.
    </div>
    """,
    unsafe_allow_html=True
)

st.markdown(
    """
    <div class="insight">
        <b>Thái Lan nổi bật nhất</b> với mức cải thiện rõ hơn.
        Việt Nam cũng cải thiện nhưng tốc độ chậm hơn,
        trong khi Singapore thay đổi tương đối ít.
    </div>
    """,
    unsafe_allow_html=True
)

st.markdown(
    """
    <div class="question">
        Điều này cho thấy quá trình số hóa và mở rộng tài khoản
        không nên được đánh giá chỉ bằng số người được kết nối.
        Cần đặt thêm câu hỏi: <b>ai thực sự được hưởng lợi?</b>
    </div>
    """,
    unsafe_allow_html=True
)

st.markdown("---")


# =========================================================
# 8. PHẦN 4 - RADAR / TỔNG HỢP
# =========================================================

st.markdown(
    '<div class="section-label">Phần 4 · Bức tranh tổng thể</div>',
    unsafe_allow_html=True
)

st.markdown(
    """
    <div class="section-title">
        Số hóa nhanh chưa chắc tạo ra một mô hình phát triển cân bằng
    </div>
    """,
    unsafe_allow_html=True
)

st.markdown(
    """
    <div class="article-text">
        Biểu đồ tổng hợp sử dụng phương pháp chuẩn hóa Min–Max trên thang điểm
        0–100 để đặt các chỉ tiêu khác đơn vị lên cùng một mặt bằng so sánh.
    </div>
    """,
    unsafe_allow_html=True
)

show_image(
    "image1.png",
    "So sánh tổng hợp các trụ cột phát triển sau chuẩn hóa Min–Max"
)

st.markdown(
    """
    <div class="article-text">
        Singapore thể hiện cấu trúc tương đối cân bằng ở các trụ cột số hóa,
        khả năng tiếp cận tài chính và bình đẳng. Thái Lan cũng có cấu trúc
        khá đồng đều.
    </div>
    """,
    unsafe_allow_html=True
)

st.markdown(
    """
    <div class="article-text">
        Việt Nam nổi bật ở tốc độ tăng trưởng và hạ tầng kết nối,
        nhưng các chỉ tiêu về khả năng tiếp cận tài chính và bình đẳng
        vẫn thấp hơn đáng kể trong phép chuẩn hóa của nhóm.
    </div>
    """,
    unsafe_allow_html=True
)

st.markdown(
    """
    <div class="insight">
        <b>Thông điệp chính:</b>
        Tốc độ số hóa cao không tự động đồng nghĩa với tài chính toàn diện.
        Điều quan trọng không chỉ là người dân có Internet,
        mà là liệu họ có thực sự tiếp cận và hưởng lợi từ các dịch vụ tài chính.
    </div>
    """,
    unsafe_allow_html=True
)

st.markdown("---")


# =========================================================
# 9. ĐIỀU BẤT NGỜ
# =========================================================

st.markdown(
    '<div class="section-label">Phát hiện đáng chú ý</div>',
    unsafe_allow_html=True
)

st.markdown(
    """
    <div class="section-title">
        Điều chúng tôi không ngờ tới
    </div>
    """,
    unsafe_allow_html=True
)

st.markdown(
    """
    <div class="article-text">
        Trước khi phân tích dữ liệu, có thể kỳ vọng rằng khi Internet
        và khả năng sở hữu tài khoản tăng, bất bình đẳng sẽ giảm theo.
    </div>

    <div class="article-text">
        Nhưng dữ liệu cho thấy một bức tranh phức tạp hơn:
        <b>một quốc gia có thể đạt mức tiếp cận tài chính rất cao
        nhưng bất bình đẳng thu nhập vẫn tồn tại.</b>
    </div>

    <div class="article-text">
        Điều này cho thấy tài chính toàn diện không chỉ là câu chuyện
        về số lượng tài khoản, mà còn liên quan đến chất lượng cơ hội
        và khả năng hưởng lợi của các nhóm dân cư khác nhau.
    </div>
    """,
    unsafe_allow_html=True
)

st.markdown("---")


# =========================================================
# 10. KẾT LUẬN
# =========================================================

st.markdown(
    '<div class="section-label">Kết luận</div>',
    unsafe_allow_html=True
)

st.markdown(
    """
    <div class="section-title">
        Từ kết nối số đến tài chính bao trùm vẫn còn một khoảng cách
    </div>
    """,
    unsafe_allow_html=True
)

st.markdown(
    """
    <div class="article-text">
        Việt Nam đang hội tụ nhanh về khả năng kết nối Internet,
        nhưng kết nối số chỉ là bước đầu tiên.
    </div>

    <div class="article-text">
        Việc người dân ngày càng sở hữu nhiều tài khoản hơn là dấu hiệu
        tích cực của tài chính toàn diện, nhưng chưa đủ để chứng minh
        rằng lợi ích của quá trình số hóa được phân phối công bằng.
    </div>

    <div class="article-text">
        Thách thức vì vậy không chỉ là đưa nhiều người lên Internet
        hoặc vào hệ thống ngân hàng, mà là bảo đảm những nhóm dễ bị
        bỏ lại phía sau cũng có khả năng tiếp cận và sử dụng hiệu quả
        các dịch vụ tài chính.
    </div>
    """,
    unsafe_allow_html=True
)

st.markdown("---")


# =========================================================
# 11. DATA & METHODOLOGY
# =========================================================

with st.expander("📚 Dữ liệu và phương pháp"):

    st.markdown(
        """
        ### Nguồn dữ liệu

        - World Bank – World Development Indicators (WDI)
        - Các số liệu được tổng hợp trong báo cáo của nhóm
        - Quốc gia: Việt Nam, Thái Lan và Singapore

        ### Các nhóm chỉ tiêu

        - Tỷ lệ dân số sử dụng Internet
        - Tỷ lệ sở hữu tài khoản tài chính
        - Hệ số Gini
        - Tăng trưởng GDP bình quân đầu người

        ### Phương pháp

        - So sánh xu hướng theo thời gian
        - So sánh giữa ba quốc gia
        - Scatter plot để quan sát mối liên hệ giữa các biến
        - Chuẩn hóa Min–Max (0–100) cho biểu đồ radar

        ### Lưu ý

        Các biểu đồ thể hiện mối liên hệ và xu hướng trong dữ liệu.
        Chúng không tự động chứng minh quan hệ nhân quả giữa số hóa,
        tài chính toàn diện và bất bình đẳng.

        Trước khi nộp sản phẩm chính thức, nhóm cần kiểm tra lại
        nguồn, năm và mức độ tương thích của từng chỉ tiêu,
        đặc biệt đối với dữ liệu Gini của Singapore.
        """
    )


# =========================================================
# 12. FOOTER
# =========================================================

st.markdown("---")

st.caption(
    "FinTech WDI Story · Việt Nam · Thái Lan · Singapore · World Bank WDI"
)