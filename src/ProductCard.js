
function ProductCard({products, index}) {
    return (
        <div className='my-16 border-black border-2 rounded-xl p-6 hover:scale-105 transition-transform'>
            <div className='text-2xl'>
                {products[index][1]}                
            </div>
            <div className='text-lg mb-2'>
                {products[index][2]}                
            </div>
            <div className='text-xs mb-2'>
                {products[index][4]}                
            </div>
            <div className="text-sm">
                {products[index][5]}                
            </div>
        </div>
    );
}

export default ProductCard;