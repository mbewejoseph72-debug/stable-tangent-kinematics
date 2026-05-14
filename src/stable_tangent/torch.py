import torch

class DirectTangentAngle(torch.nn.Module):
    """
    Differentiable version of the Direct Tangent Identity.
    Can be used inside neural networks for end-to-end training.
    """
    def forward(self, opposite, adjacent, included_angle):
        """
        opposite: side a
        adjacent: side c  
        included_angle: angle β in degrees
        """
        # Convert to radians
        inc = torch.deg2rad(included_angle)
        
        # Your direct tangent formula
        num = opposite * torch.sin(inc)
        den = adjacent - opposite * torch.cos(inc)
        
        # Use atan2 for numerical stability and correct quadrant
        return torch.rad2deg(torch.atan2(num, den))
