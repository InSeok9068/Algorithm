package 티몬.test1;

// 다음 코드를 아래 조건에 맞게 개선 하세요.

// - Template method 패턴을 이용하여 할인 금액을 하위 클래스에서 정의 할 수 있도록 개선 하세요.
// - 기존 Coupon 클래스는 500원 할인 쿠폰만을 처리하고 있습니다.
// - 기존 Coupon 클래스는 수정 할 수 없으며 새로 만들거나 상속 해야 합니다.
// - Main 메서드는 사용 예시이므로 작성하지 않아도 됩니다.
// - 500원 할인 쿠폰과 5%할인 쿠폰 Class 를 각각 정의하세요. 


public class DiscountCoupon1 extends Coupon{

    public DiscountCoupon1(int price) {
        super(price);
        // TODO Auto-generated constructor stub
    }

    public static void main(String[] args) {
        //DiscountCoupon1 discountCoupon1 = new DiscountCoupon2(1000);
        // int dp= discountCoupon1.getDiscountPrice();
        // discountCoupon1.order(dp);
    }

    private final void validate(int discountPrice) {
        if(discountPrice!=500){
            return;
        }
    }

}