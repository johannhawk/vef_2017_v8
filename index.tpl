% rebase('base.tpl')

<h2>Fyrirsögn</h2>
<div>
    % for i in range(len(products)):
       <p> <a href="/cart/add/{{ products[i]["pid"] }}"> {{ products[i]["name"] }} </a> </p>
    % end
</div>
